## Project Overview

This project develops a machine learning model to predict 10-year cardiovascular risk (coronary heart disease) using a subset of 5 clinical features from the Framingham Heart Study: age, sex, total cholesterol, hypertension status, and cigarettes per day.

The model is intended as a **proof-of-concept** to demonstrate technical skills in:
- Data preprocessing and feature selection
- Handling class imbalance with SMOTE and class weighting
- Threshold optimization prioritizing clinical sensitivity
- Model explainability using SHAP
- Deployment of an interactive web application with GPT-powered coaching

## Model Training

The model was trained in Google Colab using the Framingham Heart Study dataset (`heart_disease.csv`). The training notebooks are available in the `notebooks/` folder.

- `01_EDA.ipynb` - Exploratory data analysis and data preparation
- `02_Model_Training.ipynb` - Model training, hyperparameter tuning, feature selection, and SHAP analysis

The final trained model (`best_model.pkl`) is included in the `models/` folder and loaded directly by the Streamlit app.

## Live Demo

Test the application here:  
🔗 **[https://cardiovasculardiseaseaicoach.streamlit.app](https://cardiovasculardiseaseaicoach.streamlit.app)**

## Model Limitations

This model has several important limitations:

- **Small & generic dataset**: Trained on only 4,238 participants from a single cohort (Framingham), limiting statistical power and generalizability to diverse populations.

- **Evidence of insufficient data quality/quantity**: The model produces clinically implausible risk estimates due to the limitations of the training data. For example, a 53-year-old non-smoking male with optimal cholesterol (160 mg/dL) and no hypertension received a **40.6% 10-year risk score**, while established clinical calculators estimate ~5-10% for this healthy profile. This overestimation reflects the model's inability to learn adequate baseline risk patterns from the small and imbalanced dataset.

- **Cohort bias**: Framingham participants are predominantly white, limiting applicability to other racial/ethnic groups.

- **Missing predictors**: Does not include important risk factors such as family history, physical activity, diet, or socioeconomic status.

- **High false positive rate**: At the chosen threshold (0.366), the model produces 396 false positives per 848 patients, leading to unnecessary follow-up in a real-world setting.

- **Not clinically validated**: This model has not been prospectively validated and should not be used for medical decision-making.

## Clinical Disclaimer

This application is a **technical demonstration only**. It is not a medical device and has not been approved for clinical use. Always consult a qualified healthcare professional for medical advice.