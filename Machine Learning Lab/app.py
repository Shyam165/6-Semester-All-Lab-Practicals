from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
filename = "model.sav"
with open(filename, 'rb') as file:
    classifier = pickle.load(file)
   
filename2 = "scaler.sav"
with open(filename2, 'rb') as file2:
    sc_X = pickle.load(file2)

# Predict function
def predict_purchase(age, estimated_salary):
    input_features = np.array([[age, estimated_salary]])
    input_features = sc_X.transform(input_features)
    prediction = classifier.predict(input_features)
    return int(prediction[0])  # Convert numpy int64 to Python integer


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    age = data['age']
    estimated_salary = data['estimated_salary']
    prediction = predict_purchase(age, estimated_salary)
    return jsonify(prediction=int(prediction))


if __name__ == '__main__':
    app.run(debug=True)
