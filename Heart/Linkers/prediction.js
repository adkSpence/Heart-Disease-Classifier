function get_prediction(){
    let {PythonShell} = require('python-shell');
    const path = require("path");
    const tt = require('electron-tooltip');
        tt({
            position: 'bottom',
            width: 300,
            style: {
                backgroundColor: '#f2f3f4',
                borderRadius: '20px'
            }
        })

    // Variables that will store input and pass them to predict function as arguments
    let age = document.getElementById("age").value;
    document.getElementById("age").value = "";
    let gender = document.getElementById("gender").value;
    document.getElementById("gender").value = "";
    let chest_pain = document.getElementById("chest-pain").value;
    document.getElementById("chest-pain").value = "";
    let blood_pressure = document.getElementById("blood-pressure").value;
    document.getElementById("blood-pressure").value = "";
    let chol = document.getElementById("chol").value;
    document.getElementById("chol").value = "";
    let fbs = document.getElementById("fbs").value;
    document.getElementById("fbs").value = "";
    let ecg = document.getElementById("ecg").value;
    document.getElementById("ecg").value = "";
    let thal = document.getElementById("thal").value
    document.getElementById("thal").value = "";;
    let exang = document.getElementById("exang").value;
    document.getElementById("exang").value = "";
    let oldpeak = document.getElementById("oldpeak").value;
    document.getElementById("oldpeak").value = "";
    let slope = document.getElementById("slope").value;
    document.getElementById("slope").value = "";
    let major_vessels = document.getElementById("major-vessels").value;
    document.getElementById("major-vessels").value = "";
    let thalassemia = document.getElementById("thalassemia").value;
    document.getElementById("thalassemia").value = "";

    // Create options object
    const options = {
        scriptPath: path.join(__dirname, "/../model/"),
        args: [age, gender, chest_pain, blood_pressure, chol, fbs, ecg, thal, exang, oldpeak, slope, major_vessels, thalassemia]
    }

    // Create a python constructor using python-shell
    const prediction = new PythonShell("Predictor.py", options);

    prediction.on("message", function(message){
        if(message === "Likely chance of Myocardial Infarction"){
            swal({
                title: "Results:",
                text: "Likely chance of Myocardial Infarction",
                color: "#c62828",
                icon: "danger.png"
            })
        }
        else{
            swal({
                title: "Results:",
                text: "Unlikely chance of Myocardial Infarction",
                color: "#4caf50",
                icon: "success.svg"
            });
        }
    })
}