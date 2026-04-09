# sage-hypertension-predictor-ssa

Predicting hypertension risk in Sub-Saharan African adults using WHO SAGE data from Ghana and South Africa

## Overview

Most hypertension prediction models are trained on Western or Asian
populations. This project builds a localized, evidence-based risk tool
using real measured health data from Ghanaian and South African adults.

Built as part of the ENg 30-Day Build in Public Challenge (Data/AI Track).

## Dataset

WHO Study on Global Ageing and Adult Health (SAGE) — Wave 1 (2007–2010)  
Countries: Ghana and South Africa  
Source: https://www.icpsr.umich.edu/web/NACDA/studies/31381

Blood pressure classification follows the 2018 ESC/ESH staging system
as adopted in Ghana's national cardiovascular disease guidelines.

## Pipeline

1. Data ingestion and loading
2. Preprocessing — missing values, outliers, data types
3. Feature engineering — age-sex interaction terms, BP staging, BMI categories
4. Exploratory data analysis — hypertension trends across age, sex, and country
5. Model training — logistic regression (baseline), random forest, XGBoost
6. Evaluation and comparison — accuracy, precision, recall, AUC-ROC
7. Streamlit web app — user inputs lifestyle data, receives risk classification

## Deliverables

- Deployed Streamlit web app
- Documented Jupyter notebook
- Written summary of findings

## Progress

Built in public. Daily updates on X: @elzer252  
#ENg30DayChallenge #ENgShipIt

## Progress

Built in public. Daily updates on X: @elzer252
#ENg30DayChallenge #ENgShipIt

## Setup

1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Download data following instructions in `data/README.md`
6. Run notebooks in order from the `notebooks/` folder
