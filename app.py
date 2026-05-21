from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model and scaler

model = pickle.load(open('models/model_student_performance.pkl', 'rb'))
scaler = pickle.load(open('models/scaler_student_performance.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    # Get values from form

    sex = int(request.form['sex'])
    age = int(request.form['age'])
    Medu = int(request.form['Medu'])
    Fedu = int(request.form['Fedu'])
    Mjob = int(request.form['Mjob'])
    Fjob = int(request.form['Fjob'])
    studytime = int(request.form['studytime'])
    freetime = int(request.form['freetime'])
    goout = int(request.form['goout'])
    health = int(request.form['health'])
    absences = int(request.form['absences'])
    G1 = int(request.form['G1'])

    # Create feature array

    features = np.array([[
        sex,
        age,
        Medu,
        Fedu,
        Mjob,
        Fjob,
        studytime,
        freetime,
        goout,
        health,
        absences,
        G1
    ]])

    # Scale input

    scaled_features = scaler.transform(features)

    # Prediction

    prediction = model.predict(scaled_features)[0]

    # Result text

    if prediction == 0:
        result = "Poor Performance"
    elif prediction == 1:
        result = "Average Performance"
    else:
        result = "Excellent Performance"

    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)