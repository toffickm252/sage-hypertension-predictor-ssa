# sage-hypertension-predictor-ssa

Predicting hypertension risk in Sub-Saharan African adults using WHO SAGE data from Ghana and South Africa

## Live Demo

🚀 **[Try the app here](https://hyperpredict.streamlit.app/)**

Enter your lifestyle and demographic information to receive a hypertension risk assessment — no blood pressure reading required.

## Overview

Most hypertension prediction models are trained on Western or Asian populations. This project builds a localized, evidence-based risk tool using real measured health data from Ghanaian and South African adults.

Built as part of the ENg 30-Day Build in Public Challenge (Data/AI Track).

## Dataset

WHO Study on Global Ageing and Adult Health (SAGE) — Wave 1 (2007–2010)
Countries: Ghana (n=5,573) and South Africa (n=4,227)
Source: https://www.icpsr.umich.edu/web/NACDA/studies/31381

Blood pressure classification follows the 2018 ESC/ESH staging system as adopted in Ghana's national cardiovascular disease guidelines.

See data/README.md for download instructions.

## Pipeline

1. Data ingestion and loading ✅
2. Preprocessing — missing values, outliers, data types ✅
3. Feature engineering — age-sex interaction terms, BP staging, BMI categories ✅
4. Exploratory data analysis — hypertension trends across age, sex, and country ✅
5. Model training — logistic regression (baseline), random forest, XGBoost ✅
6. Evaluation and comparison — accuracy, precision, recall, AUC-ROC ✅
7. Streamlit web app — user inputs lifestyle data, receives risk classification ✅

## Model Performance

| Model                 | Accuracy | F1 Weighted |
| --------------------- | -------- | ----------- |
| Random Forest (tuned) | 66%      | 0.65        |
| XGBoost (tuned)       | 64%      | 0.64        |
| Logistic Regression   | 62%      | 0.63        |

**Final model:** Random Forest (n_estimators=300, min_samples_split=10, class_weight=balanced)

**Key finding:** Lifestyle and demographic factors alone can identify hypertensive status but cannot reliably stage severity. No single lifestyle factor correlates strongly with blood pressure — combined features are necessary.

## EDA Key Findings

- 60% of the combined dataset has some form of hypertension
- Hypertension severity increases with age — sharpest rise at 50-59
- South Africa carries a higher proportional hypertension burden than Ghana
- Females have slightly higher hypertension prevalence than males
- BMI increases consistently with hypertension grade
- No single lifestyle factor strongly predicts BP — the model requires combined features

## Limitations

- Dataset limited to adults aged 18+ in Ghana and South Africa only
- SAGE Wave 1 data collected 2007–2010 — may not reflect current population trends
- 66% accuracy reflects the inherent complexity of predicting hypertension from lifestyle data alone
- Clinical blood pressure measurement remains necessary for diagnosis

## Future Work

- Incorporate SAGE Wave 2 and Wave 3 data for longitudinal analysis
- Expand to additional African countries as data becomes available
- Explore deep learning approaches with larger datasets
- Formal academic publication with extended literature review

## Deliverables

- [x] Deployed Streamlit web app — https://hyperpredict.streamlit.app/
- [x] Documented Jupyter notebooks
- [x] Trained and saved Random Forest model
- [x] Written summary of findings

## Project Structure

```
sage-hypertension-predictor-ssa/
├── README.md
├── requirements.txt
├── data/
│   └── README.md
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_eda.ipynb
│   └── 05_model_training.ipynb
├── models/
│   ├── hypertension_model.joblib
│   └── scaler.joblib
├── app/
│   ├── app.py
│   └── requirements.txt
└── docs/
    └── findings_summary.md
```

## Setup

1. Clone the repo
2. Create a virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Download data following instructions in `data/README.md`
6. Run notebooks in order from the `notebooks/` folder

## Citation

If you use this project, please cite the WHO SAGE dataset:

Chatterji, S., and Kowal, P. WHO Study on Global AGEing and Adult Health (SAGE): Wave 1, 2007-2010. ICPSR31381-v1. Ann Arbor, MI: Inter-university Consortium for Political and Social Research, 2013.

## Progress

Built in public. Daily updates on X: @elzer252
#ENg30DayChallenge #ENgShipIt
