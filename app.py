import streamlit as st
from joblib import load

# load the model
model = load('model.joblib')

# create a function to predict the demand
def predict_demand(features):
    features = [features]
    prediction = model.predict(features)
    return prediction

# create the UI for the app
st.title('Demand Prediction App')
st.write('This app predicts the demand for a product based on the features provided.')

feature1 = st.number_input('Total Price')
feature2 = st.number_input('Base Price')

if st.button('Predict Demand'):
    features = [feature1, feature2]
    prediction = predict_demand(features)
    st.write(f'The predicted demand is: {prediction[0]}')
