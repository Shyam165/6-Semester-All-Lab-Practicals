import streamlit as st
import pickle
import numpy as np

# Loading the the saved model
with open('model8.sav', 'rb') as file:
    model = pickle.load(file)

def predict_clusters(data):
    clusters = model.fit_predict(data)

    labels = ['Careless', 'Standard', 'Target', 'Careful', 'Sensible']
    return [labels[cluster] for cluster in clusters]


def main():
    st.title('Customer Segmentation Prediction')
    st.sidebar.header('User Input')

    data = []
    for i in range(5):
        annual_income = st.sidebar.number_input(f'Sample {i+1}: Annual Income', min_value=0, max_value=200, step=1)
        spending_score = st.sidebar.number_input(f'Sample {i+1}: Spending Score', min_value=0, max_value=100,step=1)
        data.append([annual_income, spending_score])

    if st.sidebar.button('Predict'):
        labels = predict_clusters(data)
        st.subheader("Prediction Results:")
        for i, label in enumerate(labels):
            st.success(f"Sample {i+1}: {label}")

if __name__ == '__main__':
    main()
