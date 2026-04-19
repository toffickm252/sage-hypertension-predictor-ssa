import os

import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and scaler
# Get the directory of this file and build path to models
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, 'models', 'hypertension_model.joblib'))
scaler = joblib.load(os.path.join(BASE_DIR, 'models', 'scaler.joblib'))

st.title('Hypertension Risk Predictor')
st.subheader('Sub-Saharan Africa — Ghana & South Africa')
st.write('Enter your lifestyle and demographic information to assess your hypertension risk.')

## Personal Information
st.header('Personal Information')
col1, col2 = st.columns(2)

with col1:
    country = st.selectbox('Country', ['Ghana', 'South Africa'])
    age = st.number_input('Age (years)', min_value=18, max_value=110, value=40)

with col2:
    residence = st.selectbox('Residence', ['Urban', 'Rural'])
    sex = st.selectbox('Sex', ['Male', 'Female'])

## Body measurements
st.header('Body Measurements')
col3, col4 = st.columns(2)

with col3:
    height = st.number_input('Height (cm)', min_value=100, max_value=220, value=165)
    waist = st.number_input('Waist Circumference (cm)', min_value=40, max_value=200, value=80)

with col4:
    weight = st.number_input('Weight (kg)', min_value=30, max_value=200, value=70)
    hip = st.number_input('Hip Circumference (cm)', min_value=40, max_value=200, value=90)

## Tobacco use 
st.header('Tobacco Use')
col5, col6 = st.columns(2)

with col5:
    ever_tobacco = st.selectbox('Ever used tobacco?', ['No', 'Yes'])

with col6:
    current_tobacco = st.selectbox('Currently use tobacco?', ['No', 'Yes'])

## alcohol Use 
st.header('Alcohol Use')
col7, col8 = st.columns(2)

with col7:
    ever_alcohol = st.selectbox('Ever used alcohol?', ['No', 'Yes'])
    recent_alcohol = st.selectbox('Alcohol in last 30 days?', ['No', 'Yes'])

with col8:
    avg_drinks = st.number_input('Average drinks per day', min_value=0, max_value=20, value=0)

## Personal Activity
st.header('Physical Activity')
col9, col10 = st.columns(2)

with col9:
    vigorous_work = st.selectbox('Vigorous work activity?', ['No', 'Yes'])
    days_vigorous = st.number_input('Days vigorous work per week', min_value=0, max_value=7, value=0)
    moderate_work = st.selectbox('Moderate work activity?', ['No', 'Yes'])

with col10:
    walks = st.selectbox('Walk or cycle regularly?', ['No', 'Yes'])
    vigorous_leisure = st.selectbox('Vigorous leisure activity?', ['No', 'Yes'])
    moderate_leisure = st.selectbox('Moderate leisure activity?', ['No', 'Yes'])

## Diet choices
st.header('Diet')
col11, col12 = st.columns(2)

with col11:
    fruit = st.number_input('Fruit servings per day', min_value=0, max_value=20, value=2)

with col12:
    veg = st.number_input('Vegetable servings per day', min_value=0, max_value=20, value=2)

## Prediction
## st.button('Predict My Risk',key='predict_button')
if st.button('Predict My Risk', key='predict_button'):
    
    # Encode inputs
    country_code = 241 if country == 'Ghana' else 155
    residence_code = 1 if residence == 'Urban' else 2
    sex_code = 1 if sex == 'Male' else 0
    bmi = weight / ((height / 100) ** 2)
    age_sex = age * sex_code

    def yn(val):
        return 1 if val == 'Yes' else 0

    features = pd.DataFrame([[
        country_code, residence_code, age,
        height, weight, waist, hip,
        yn(ever_tobacco), yn(current_tobacco),
        yn(ever_alcohol), yn(recent_alcohol), avg_drinks,
        yn(vigorous_work), days_vigorous, yn(moderate_work),
        yn(walks), yn(vigorous_leisure), yn(moderate_leisure),
        fruit, veg, bmi, sex_code, age_sex
    ]], columns=[
        'country', 'residence', 'age',
        'height_cm', 'weight_kg', 'waist_cm', 'hip_cm',
        'ever_tobacco', 'current_tobacco',
        'ever_alcohol', 'recent_alcohol', 'avg_drinks_daily',
        'vigorous_work', 'days_vigorous_work', 'moderate_work',
        'walks_or_cycles', 'vigorous_leisure', 'moderate_leisure',
        'fruit_servings', 'veg_servings', 'bmi', 'sex_encoded', 'age_sex_interaction'
    ])

    # Scale features and predict
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0][1]

    # Display result
    st.divider()
    if prediction == 1:
        st.error(f'⚠️ High Hypertension Risk Detected')
        st.write(f'Risk probability: **{probability:.0%}**')
        st.write('Please consult a healthcare provider for a clinical blood pressure assessment.')
    else:
        st.success(f'✅ Low Hypertension Risk')
        st.write(f'Risk probability: **{probability:.0%}**')
        st.write('Maintain your healthy lifestyle. Regular check-ups are still recommended.')
    
    st.info(f'Calculated BMI: {bmi:.1f}')