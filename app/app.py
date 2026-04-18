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

st.header('Personal Information')
st.header('Body Measurements')
st.header('Tobacco Use')
st.header('Alcohol Use')
st.header('Physical Activity')
st.header('Diet')

st.button('Predict My Risk')