import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import time
from sklearn.externals import joblib
import warnings

warnings.filterwarnings('ignore')


def timer(f):
    start_time = time.time()
    results = f()
    end_time = time.time()
    print("Training time: {}".format(end_time - start_time))

    return results


def model_for_data(features, target, algo):
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.25, random_state=0)
    pipeline = make_pipeline(algo)
    model = timer(lambda: pipeline.fit(X_train, y_train))

    return X_test, y_test, model


# Reading datafile into dataframe
heart_data = pd.read_csv('dataset/heart.csv')
heart_data.drop_duplicates(inplace=True)

estimators = heart_data.drop(['target'], axis=1)
labels = heart_data.target.values

tests_input, tests_output, heart_model = model_for_data(features=estimators, target=labels, algo=LogisticRegression())

predictions = heart_model.predict(tests_input)
print(f"{round(accuracy_score(y_true=tests_output, y_pred=predictions)*100, 2)}%")

save_model = joblib.dump(value=heart_model, filename='result/heart_model.pkl')
