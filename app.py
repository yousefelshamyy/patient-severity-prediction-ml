import streamlit as st
import pandas as pd
import pickle


# =========================
# Load Model
# =========================
@st.cache_resource
def load_model():
    with open("Patient_Servey.pkl", "rb") as f:
        return pickle.load(f)


pipeline = load_model()


# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Patient Severity Predictor",
    page_icon="🏥",
    layout="centered"
)


# =========================
# Title
# =========================
st.markdown("""
<h1 style='text-align:center;color:#2E86C1;'>
🏥 Patient Severity Prediction App
</h1>
""", unsafe_allow_html=True)


st.divider()


# =========================
# Inputs
# =========================

col1, col2 = st.columns(2)


with col1:
    age = st.number_input("Age", 0, 120, 30)

    bmi = st.number_input(
        "BMI",
        10.0,
        60.0,
        25.0
    )

    blood_pressure_systolic = st.number_input(
        "BP Systolic",
        50,
        250,
        120
    )

    glucose_level = st.number_input(
        "Glucose Level",
        50,
        500,
        90
    )


with col2:

    cholesterol = st.number_input(
        "Cholesterol",
        100,
        400,
        180
    )

    wbc_count = st.number_input(
        "WBC Count",
        1000,
        30000,
        7000
    )


    smoking_status = st.selectbox(
        "Smoking Status",
        [
            "Never Smoked",
            "Former Smoker",
            "Smokes"
        ]
    )


    diabetes = st.selectbox(
        "Diabetes",
        [
            "Yes",
            "No"
        ]
    )



# =========================
# Gender
# =========================

gender = st.selectbox(
    "Gender",
    [
        "Male",
        "Female"
    ]
)


st.divider()



# =========================
# Prediction
# =========================

if st.button(
    "🔮 Predict",
    use_container_width=True
):

    input_data = pd.DataFrame({

        "age":[age],

        "bmi":[bmi],

        "blood_pressure_systolic":
        [blood_pressure_systolic],

        "glucose_level":
        [glucose_level],

        "cholesterol":
        [cholesterol],

        "wbc_count":
        [wbc_count],

        "gender":
        [gender],

        "smoking_status":
        [smoking_status],

        "diabetes":
        [diabetes]
    })


    prediction = pipeline.predict(input_data)[0]


    st.success(
        f"📊 Predicted Severity: {prediction}"
    )