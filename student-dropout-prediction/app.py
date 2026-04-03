import streamlit as st
import pandas as pd
import joblib

# Load model & features
model = joblib.load("model/model.pkl")
features = joblib.load("model/features.pkl")

st.title("🎓 Student Dropout Prediction")

# ======================
# INPUT USER (WAJIB DI ATAS)
# ======================

age = st.number_input("Age at Enrollment", 17, 60)
admission = st.number_input("Admission Grade", 0.0, 200.0)
tuition = st.selectbox("Tuition Fees Up To Date", [0, 1])

approved_1 = st.number_input("Approved 1st Semester", 0, 10)
approved_2 = st.number_input("Approved 2nd Semester", 0, 10)

grade_1 = st.number_input("Grade 1st Semester", 0.0, 20.0)
grade_2 = st.number_input("Grade 2nd Semester", 0.0, 20.0)

# ======================
# FEATURE ENGINEERING
# ======================

total_approved = approved_1 + approved_2
avg_grade = (grade_1 + grade_2) / 2

# ======================
# PREPARE INPUT (FULL FEATURES)
# ======================

input_dict = {col: 0 for col in features}

input_dict.update(
    {
        "Age_at_enrollment": age,
        "Admission_grade": admission,
        "Tuition_fees_up_to_date": tuition,
        "Curricular_units_1st_sem_approved": approved_1,
        "Curricular_units_2nd_sem_approved": approved_2,
        "Curricular_units_1st_sem_grade": grade_1,
        "Curricular_units_2nd_sem_grade": grade_2,
        "total_approved": total_approved,
        "avg_grade": avg_grade,
    }
)

input_df = pd.DataFrame([input_dict])

# ======================
# PREDICTION
# ======================

if st.button("Predict"):
    pred = model.predict(input_df)[0]

    if pred == 1:
        st.error("⚠️ High Risk of Dropout")
    else:
        st.success("✅ Low Risk")
