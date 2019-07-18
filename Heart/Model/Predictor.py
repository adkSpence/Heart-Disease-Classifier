import numpy as np
from sklearn.externals import joblib
import warnings
import sys, os

warnings.filterwarnings('ignore')

age = sys.argv[1]
gender = sys.argv[2]
chest_pain = sys.argv[3]
blood_pressure = sys.argv[4]
chol = sys.argv[5]
fbs = sys.argv[6]
ecg = sys.argv[7]
thal = sys.argv[8]
exang = sys.argv[9]
oldpeak = sys.argv[10]
slope = sys.argv[11]
major_vessels = sys.argv[12]
thalassemia = sys.argv[13]

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'result\\heart_model.pkl')
heart_model = joblib.load(my_file)

features = [float(age), float(gender), float(chest_pain), float(blood_pressure), float(chol), float(fbs), float(ecg), float(thal), float(exang), float(oldpeak), float(slope), float(major_vessels), float(thalassemia)]
features = np.array(features).reshape(1, -1)

result = np.asscalar(heart_model.predict(features))

if result == 1:
    print("Likely chance of Myocardial Infarction")
else:
    print("Unlikely chance of Myocardial Infarction")


sys.stdout.flush()
