import streamlit as st
import joblib
import os

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), 'retail_model.joblib')
model = joblib.load(model_path)

# Simple UI
st.title("Retail Sales Predictor")

gender = st.selectbox("Select Gender", ['Male', 'Female'])
age = st.slider("Select Age", 18, 70, 30)
category = st.selectbox("Select Product Category", ['Clothing', 'Electronics', 'Home', 'Grocery'])

if st.button("Predict"):
    input_df = pd.DataFrame([[gender, age, category]], columns=['Gender', 'Age', 'Product Category'])
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Total Amount: ${prediction:.2f}")
