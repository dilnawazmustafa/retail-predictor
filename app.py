import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open('retail_model.pkl', 'rb'))

st.title("🛍️ Retail Sales Prediction App")
st.write("Enter details to predict the total purchase amount.")

# Inputs
gender = st.selectbox("Gender", ["Female", "Male"])
age = st.slider("Age", 18, 70)
category = st.selectbox("Product Category", ["Clothing", "Electronics", "Groceries"])

# Encode inputs
gender_num = 1 if gender == "Male" else 0
category_map = {"Clothing": 0, "Electronics": 1, "Groceries": 2}
category_num = category_map[category]

# Build sample
sample = pd.DataFrame({
    'Gender': [gender_num],
    'Age': [age],
    'Product Category': [category_num]
})

# Predict
if st.button("Predict"):
    prediction = model.predict(sample)
    st.success(f"💰 Predicted Total Amount: ${prediction[0]:.2f}")
