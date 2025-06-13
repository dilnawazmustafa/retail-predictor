import streamlit as st
import pandas as pd
import joblib
import os

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'retail_model.joblib')
model = joblib.load(model_path)

st.title("🛍️ Retail Sales Predictor")
st.write("Enter customer details to predict the total purchase amount.")

# Inputs
gender = st.selectbox("Select Gender", ["Male", "Female"])
age = st.slider("Select Age", 18, 70, 30)
category = st.selectbox("Select Product Category", ["Clothing", "Electronics", "Home", "Grocery"])

# Predict button
if st.button("Predict"):
    # Convert string inputs to numeric as expected by model
    gender_num = 1 if gender == "Male" else 0

    category_map = {
        "Clothing": 0,
        "Electronics": 1,
        "Home": 2,
        "Grocery": 3
    }
    category_num = category_map[category]

    # Create input dataframe for the model
    input_df = pd.DataFrame([[gender_num, age, category_num]], columns=['Gender', 'Age', 'Product Category'])

    # Predict
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Total Amount: ${prediction:.2f}")
