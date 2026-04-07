## Model Training

The model was trained in Google Colab using the NHANES dataset. The training notebooks are available in the `notebooks/` folder:

- `01_EDA.ipynb` - Exploratory data analysis and data preparation
- `02_Model_Training.ipynb` - Model training, hyperparameter tuning, feature selection, and SHAP analysis

The final trained model (`best_model.pkl`) is included in the `models/` folder and loaded directly by the Streamlit app.