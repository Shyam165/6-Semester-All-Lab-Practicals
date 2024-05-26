from flask import Flask, request, render_template
import pickle
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained KMeans model
filename = "model7.sav"
with open(filename, 'rb') as file:
    kmeans = pickle.load(file)

# Define a route for the default URL, which loads the form
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        try:
            # Get data from form
            annual_income = float(request.form['annual_income'])
            spending_score = float(request.form['spending_score'])

            # Make prediction
            predict = kmeans.predict([[annual_income, spending_score]])

            # Determine the customer type based on the prediction
            if predict == [0]:
                prediction = "Customer is careless"
            elif predict == [1]:
                prediction = "Customer is standard"
            elif predict == [2]:
                prediction = "Customer is Target"
            elif predict == [3]:
                prediction = "Customer is careful"
            else:
                prediction = "Customer is sensible"

        except Exception as e:
            prediction = f"Error: {str(e)}"
    
    return render_template('index.html', prediction=prediction)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
