import streamlit as st
import numpy as np
import pickle
from PIL import Image

# Load the pre-trained pipeline from the saved model file
with open("Models/model.sav", "rb") as file:
    pipeline = pickle.load(file)

# Function to make predictions
def predict_purchase(age, estimated_salary):
    # Use the pipeline for prediction
    output = pipeline.predict([[age, estimated_salary]])
    return output[0]

# Streamlit app
st.title("Purchase Prediction App")
st.write("Welcome to the Purchase Prediction App! This app predicts whether a customer will purchase an item based on their age and estimated salary.")

# Load an image for better visualization
image = Image.open("Models/th.jpeg")
st.image(image, caption="Image by Gerd Altmann from Pixabay", use_column_width=True)

# User input for age
age = st.number_input("Enter Age", min_value=0, max_value=120, value=34)

# User input for estimated salary
estimated_salary = st.number_input("Enter Estimated Salary", min_value=0, value=765580)

# Button to make prediction
if st.button("Predict"):
    # Make prediction
    prediction = predict_purchase(age, estimated_salary)
    
    # Display prediction result
    st.subheader("Prediction Result:")
    if prediction == 1:
        st.success("Item will be purchased")
    else:
        st.error("Item will not be purchased")
