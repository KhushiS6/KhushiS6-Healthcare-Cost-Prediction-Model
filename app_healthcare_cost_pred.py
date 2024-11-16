# -*- coding: utf-8 -*-
"""app_healthcare_cost_pred.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d1UxBgJ7tYKN1Wxzi8F-jGBDfv8WG9TW
"""

import streamlit as st
import joblib
import numpy as np

# Load model and preprocessing files
model = joblib.load('healthcare_cost_prediction_model.joblib')
scaler = joblib.load('scaler.joblib')
label_encoders = joblib.load('label_encoders.joblib')

# Set page title, icon, and layout
st.set_page_config(page_title="Healthcare Cost Prediction", layout="wide", page_icon="🩺")

# Header and description with icons
st.markdown("# Healthcare Cost Prediction App 🏥", unsafe_allow_html=True)
st.markdown("""
    **Developed by Khushi**  
    Predict healthcare costs based on patient profiles and admission details.  
    This app uses advanced machine learning models to estimate the healthcare cost, so you can make informed decisions.
    """, unsafe_allow_html=True)

# Input form for patient details
with st.form("prediction_form"):
    st.subheader("Enter Patient Details")
    
    hospital = st.selectbox("Hospital", label_encoders['Hospital'].classes_, index=0, help="Select the hospital name", key="hospital")
    age = st.number_input("Age", min_value=0, max_value=120)
    length_of_stay = st.number_input("Length of Stay (days)", min_value=0, max_value=365)
    blood_type = st.selectbox("Blood Type", label_encoders['Blood Type'].classes_, index=0, key="blood_type")
    medical_condition = st.selectbox("Medical Condition", label_encoders['Medical Condition'].classes_, index=0, key="medical_condition")
    insurance_provider = st.selectbox("Insurance Provider", label_encoders['Insurance Provider'].classes_, index=0, key="insurance_provider")
    medication = st.selectbox("Medication", label_encoders['Medication'].classes_, index=0, key="medication")
    admission_type = st.selectbox("Admission Type", label_encoders['Admission Type'].classes_, index=0, key="admission_type")
    test_results = st.selectbox("Test Results", label_encoders['Test Results'].classes_, index=0, key="test_results")
    gender = st.selectbox("Gender", label_encoders['Gender'].classes_, index=0, key="gender")

    # Add a submit button for the form
    submit_button = st.form_submit_button(label="Predict Healthcare Cost")

# Prepare inputs for prediction
if submit_button:
    inputs = np.array([
        label_encoders['Hospital'].transform([hospital])[0],
        age,
        length_of_stay,
        label_encoders['Blood Type'].transform([blood_type])[0],
        label_encoders['Medical Condition'].transform([medical_condition])[0],
        label_encoders['Insurance Provider'].transform([insurance_provider])[0],
        label_encoders['Medication'].transform([medication])[0],
        label_encoders['Admission Type'].transform([admission_type])[0],
        label_encoders['Test Results'].transform([test_results])[0],
        label_encoders['Gender'].transform([gender])[0]
    ]).reshape(1, -1)

    # Scale numerical features
    inputs[:, 1:3] = scaler.transform(inputs[:, 1:3])

    # Display prediction result
    prediction = model.predict(inputs)
    st.markdown(f"### Predicted Healthcare Cost: ${prediction[0]:,.2f}", unsafe_allow_html=True)

    # Feedback section after prediction
    st.markdown("""
    ## We Value Your Feedback! ✍️  
    Please leave your comments or suggestions to help improve this app.
    """, unsafe_allow_html=True)

    # Collect feedback
    feedback = st.text_area("Enter your feedback or comments here:", height=150)

    # Submit feedback button
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your valuable feedback!")
        else:
            st.warning("Please enter some feedback before submitting.")

# Add a section with a button that links to Khushi's GitHub
st.markdown("## About the Developer 💻")
st.markdown("""
    The app is developed by **Khushi**.  
    You can find more of her work and contribute to her projects via her GitHub profile.
""", unsafe_allow_html=True)

# GitHub Link Button with better styling and colors
if st.button("Visit GitHub Profile"):
    js = "window.open('https://github.com/KhushiS6')"
    st.markdown(f'<a href="javascript:{js}"><button class="stButton">Go to GitHub Profile</button></a>', unsafe_allow_html=True)

# Customize app styling (optional)
st.markdown(
    """
    <style>
    /* Styling the 'Go to GitHub' button */
    .stButton {
        background-color: #2D9CDB;
        color: white;
        font-size: 18px;
        padding: 14px 28px;
        border: none;
        cursor: pointer;
        border-radius: 8px;
        width: 100%;
        text-align: center;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .stButton:hover {
        background-color: #1F77B4;
    }

    /* Styling the input and feedback area */
    .stTextInput textarea {
        font-size: 16px;
        padding: 12px;
        border-radius: 8px;
        width: 100%;
        box-sizing: border-box;
        border: 1px solid #ddd;
        margin-bottom: 15px;
    }
    .stTextInput label {
        font-weight: bold;
    }

    /* Styling the title and headers */
    h1, h2, h3 {
        font-family: 'Roboto', sans-serif;
        color: #2c3e50;
    }

    h1 {
        font-size: 32px;
        margin-bottom: 10px;
    }

    h2, h3 {
        font-size: 24px;
        margin-bottom: 5px;
    }

    .stText {
        font-size: 18px;
        font-weight: normal;
        color: #7f8c8d;
    }

    /* Custom button for 'Go to GitHub' */
    .stButton {
        background-color: #2D9CDB;
        color: white;
        font-size: 18px;
        padding: 14px 28px;
        border-radius: 8px;
        text-align: center;
        cursor: pointer;
        border: none;
        width: 100%;
        transition: background-color 0.3s ease;
    }

    .stButton:hover {
        background-color: #1F77B4;
    }
    </style>
    """, unsafe_allow_html=True
)
