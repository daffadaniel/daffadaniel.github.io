import streamlit as st
import pandas as pd
from src.modelling import predict  

st.set_page_config(page_title="Used Car Price Prediction", layout="centered")

st.title("🚗 Used Car Price Prediction")

st.write("Enter your car's details to predict its price:")

# Form input
with st.form("car_form"):
    # Input text
    brand = st.text_input("Brand", "Toyota")
    model = st.text_input("Model", "Camry")

    # Input Number
    model_year = st.number_input("Model Year", min_value=1980, max_value=2025, value=2019)
    milage = st.number_input("Milage (km)", min_value=0, value=25000)

    # Input  (dropdown)
    fuel_type = st.selectbox("Fuel Type", ["Gasoline", "Diesel", "Hybrid", "Electric"])
    engine = st.text_input("Engine", "2.5L I4")
    transmission = st.selectbox("Transmission", ["Automatic", "Manual"])
    ext_col = st.text_input("Exterior Color", "Black")
    int_col = st.text_input("Interior Color", "Beige")
    accident = st.selectbox("Accident", ["Yes", "No"])
    clean_title = st.selectbox("Clean Title", ["Yes", "No"])

    # submit button
    submitted = st.form_submit_button("Price Prediction")

if submitted:
    # Make a 1 row dataframe as input
    input_data = pd.DataFrame([{
        "brand": brand,
        "model": model,
        "model_year": model_year,
        "milage": milage,
        "fuel_type": fuel_type,
        "engine": engine,
        "transmission": transmission,
        "ext_col": ext_col,
        "int_col": int_col,
        "accident": accident,
        "clean_title": clean_title
    }])

    try:
        pred = predict(input_data)
        st.success(f"Car Price Prediction: **${pred[0]:,.2f}**")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")