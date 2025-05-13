import streamlit as st
import numpy as np
import joblib

model = joblib.load('Linear_Regression.joblib')

st.title("Job Package Prediction Based on CGPA")
st.write("Enter your CGPA to predict the expected job package:")

cgpa = st.number_input("CGPA",min_value=3.0,max_value=10.0,step=0.1)

if st.button("Predict Package"):
    
    prediction = model.predict(np.array([[cgpa]]))
    predicted_value = float(prediction[0])
    
    st.success(f"Predicted Package : ${predicted_value:.2f} LPA")