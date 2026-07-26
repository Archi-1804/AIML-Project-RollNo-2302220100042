import streamlit as st
import pandas as pd
import joblib

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    page_icon="🏥",
    layout="centered"
)

# -------------------------
# Load Model
# -------------------------
model = joblib.load("model/insurance_model.pkl")
columns = joblib.load("model/columns.pkl")

# -------------------------
# Title
# -------------------------
st.title("🏥 Medical Insurance Cost Prediction")
st.write("Predict your annual medical insurance charges using Machine Learning.")

st.markdown("---")

# -------------------------
# User Inputs
# -------------------------

age = st.slider("Age", 18, 65, 25)

sex = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

bmi = st.slider(
    "BMI",
    15.0,
    50.0,
    24.0,
    step=0.1
)

children = st.slider(
    "Children",
    0,
    5,
    0
)

smoker = st.selectbox(
    "Smoking Status",
    ["No", "Yes"]
)

region = st.selectbox(
    "Region",
    [
        "Northeast",
        "Northwest",
        "Southeast",
        "Southwest"
    ]
)

st.markdown("---")

# -------------------------
# Prediction
# -------------------------

if st.button("Predict Insurance Charges"):

    # Create dataframe
    data = {
        "age": age,
        "bmi": bmi,
        "children": children,

        "sex_male": 1 if sex == "Male" else 0,

        "smoker_yes": 1 if smoker == "Yes" else 0,

        "region_northwest": 1 if region == "Northwest" else 0,
        "region_southeast": 1 if region == "Southeast" else 0,
        "region_southwest": 1 if region == "Southwest" else 0,

        "bmi_category_Obese": 1 if bmi >= 30 else 0,
        "bmi_category_Overweight": 1 if 25 <= bmi < 30 else 0,
        "bmi_category_Underweight": 1 if bmi < 18.5 else 0,

        "smoker_bmi": (1 if smoker == "Yes" else 0) * bmi
    }

    input_df = pd.DataFrame([data])

    # Ensure same column order
    input_df = input_df[columns]

    prediction = model.predict(input_df)[0]

    st.success(f"Estimated Annual Insurance Charges: ₹ {prediction:,.2f}")

    st.markdown("---")

    if prediction < 10000:
        st.info("🟢 Low Estimated Insurance Cost")

    elif prediction < 25000:
        st.warning("🟡 Medium Estimated Insurance Cost")

    else:
        st.error("🔴 High Estimated Insurance Cost")