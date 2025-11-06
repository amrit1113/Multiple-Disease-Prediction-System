# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 01:35:45 2025

@author: Lenovo
"""

import numpy as np
import pickle
import streamlit as st
import os
from streamlit_option_menu import option_menu

# =======================
# Load the Saved Models
# =======================

import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'diabetes_model.sav'), 'rb') as f:
    diabetes_model = pickle.load(f)

with open(os.path.join(BASE_DIR, 'heart_disease_model.sav'), 'rb') as f:
    heart_disease_model = pickle.load(f)

with open(os.path.join(BASE_DIR, 'covid_prediction_model.sav'), 'rb') as f:
    covid_model = pickle.load(f)



# =======================
# Sidebar Navigation
# =======================
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Covid 19 Prediction'],
        icons=['activity', 'heart', 'mask'],
        default_index=0
    )


# =======================
# Diabetes Prediction Page
# =======================
if selected == 'Diabetes Prediction':

    st.title('🩸 Diabetes Prediction System')

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    # Prediction
    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[float(Pregnancies), float(Glucose), float(BloodPressure),
                                                       float(SkinThickness), float(Insulin), float(BMI),
                                                       float(DiabetesPedigreeFunction), float(Age)]])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is Diabetic 😟'
            else:
                diab_diagnosis = 'The person is Not Diabetic 😊'
        except:
            diab_diagnosis = '⚠️ Please enter valid numeric values.'

    st.success(diab_diagnosis)


# =======================
# Heart Disease Prediction Page
# =======================
if selected == 'Heart Disease Prediction':

    st.title('❤️ Heart Disease Prediction System')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
    with col3:
        cp = st.text_input('Chest Pain Type (0-3)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0-2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0-2)')
    with col3:
        ca = st.text_input('Number of major vessels (0-3) colored by fluoroscopy')
    with col1:
        thal = st.text_input('Thalassemia (0 = normal, 1 = fixed defect, 2 = reversible defect)')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_model.predict([[float(age), float(sex), float(cp), float(trestbps),
                                                     float(chol), float(fbs), float(restecg), float(thalach),
                                                     float(exang), float(oldpeak), float(slope), float(ca),
                                                     float(thal)]])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has Heart Disease 💔'
            else:
                heart_diagnosis = 'The person does not have Heart Disease ❤️'
        except:
            heart_diagnosis = '⚠️ Please enter valid numeric values.'

    st.success(heart_diagnosis)


# =======================
# Covid-19 Prediction Page 
# =======================
if selected == 'Covid 19 Prediction':

    st.title('😷 COVID-19 Prediction System')

    st.markdown("Enter 1 for **Yes**, and 0 for **No** in all the fields below:")

    col1, col2, col3 = st.columns(3)

    with col1:
        Breathing_Problem = st.text_input('Breathing Problem (1/0)')
        Fever = st.text_input('Fever (1/0)')
        Dry_Cough = st.text_input('Dry Cough (1/0)')
        Sore_Throat = st.text_input('Sore Throat (1/0)')
        Running_Nose = st.text_input('Running Nose (1/0)')
        Asthma = st.text_input('Asthma (1/0)')
        Chronic_Lung_Disease = st.text_input('Chronic Lung Disease (1/0)')

    with col2:
        Headache = st.text_input('Headache (1/0)')
        Heart_Disease = st.text_input('Heart Disease (1/0)')
        Diabetes = st.text_input('Diabetes (1/0)')
        Hyper_Tension = st.text_input('Hyper Tension (1/0)')
        Fatigue = st.text_input('Fatigue (1/0)')
        Gastrointestinal = st.text_input('Gastrointestinal (1/0)')

    with col3:
        Abroad_travel = st.text_input('Abroad Travel (1/0)')
        Contact_with_COVID_Patient = st.text_input('Contact with COVID Patient (1/0)')
        Attended_Large_Gathering = st.text_input('Attended Large Gathering (1/0)')
        Visited_Public_Exposed_Places = st.text_input('Visited Public Exposed Places (1/0)')
        Family_working_in_Public_Exposed_Places = st.text_input('Family working in Public Exposed Places (1/0)')
        Wearing_Masks = st.text_input('Wearing Masks (1/0)')
        Sanitization_from_Market = st.text_input('Sanitization from Market (1/0)')

    covid_diagnosis = ''

    if st.button('Covid Test Result'):
        try:
            covid_prediction = covid_model.predict([[ 
                float(Breathing_Problem), float(Fever), float(Dry_Cough), float(Sore_Throat),
                float(Running_Nose), float(Asthma), float(Chronic_Lung_Disease), float(Headache),
                float(Heart_Disease), float(Diabetes), float(Hyper_Tension), float(Fatigue),
                float(Gastrointestinal), float(Abroad_travel), float(Contact_with_COVID_Patient),
                float(Attended_Large_Gathering), float(Visited_Public_Exposed_Places),
                float(Family_working_in_Public_Exposed_Places), float(Wearing_Masks),
                float(Sanitization_from_Market)
            ]])

            if covid_prediction[0] == 1:
                covid_diagnosis = '😷 The person is likely COVID-19 Positive'
            else:
                covid_diagnosis = '😊 The person is likely COVID-19 Negative'

        except Exception as e:
            covid_diagnosis = f'⚠️ Please enter valid numeric values.\n\nError: {e}'

    st.success(covid_diagnosis)
