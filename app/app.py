import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and scaler
model = joblib.load('.../models/hypertension_model.joblib')
scaler = joblib.load('.../models/scaler.joblib')

st.title('Hypertension Risk Predictor')
st.subheader('Sub-Saharan Africa — Ghana & South Africa')
st.write('Enter your lifestyle and demographic information to assess your hypertension risk.')