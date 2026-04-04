import streamlit as st
import pandas as pd
import joblib
import os

# ======================
# LOAD MODEL (FIX PATH CLOUD)
# ======================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "model", "model.pkl")
features_path = os.path.join(BASE_DIR, "model", "features.pkl")

model = joblib.load(model_path)
features = joblib.load(features_path)

# ======================
# UI
# ======================

st.set_page_config(page_title="Dropout Prediction", layout="centered")

st.title("🎓 Student Dropout Prediction")
st.markdown("Masukkan data mahasiswa untuk memprediksi risiko dropout.")

# ======================
# INPUT USER
# ======================

st.subheader("📊 Academic & Financial Data")

age = st.number_input("Age at Enrollment", 17, 60, value=20)
admission = st.number_input("Admission Grade", 0.0, 200.0, value=120.0)
tuition = st.selectbox("Tuition Fees Up To Date", [0, 1])

approved_1 = st.number_input("Approved Units - 1st Semester", 0, 10, value=3)
approved_2 = st.number_input("Approved Units - 2nd Semester", 0, 10, value=3)

grade_1 = st.number_input("Grade - 1st Semester", 0.0, 20.0, value=12.0)
grade_2 = st.number_input("Grade - 2nd Semester", 0.0, 20.0, value=12.0)

# ======================
# FEATURE ENGINEERING
# ======================

total_approved = approved_1 + approved_2
avg_grade = (grade_1 + grade_2) / 2

# ======================
# PREPARE INPUT
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

st.subheader("🔍 Prediction Result")

if st.button("Predict"):
    try:
        pred = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0][1]

        if pred == 1:
            st.error("⚠️ High Risk of Dropout")
            st.write(
                "Mahasiswa disarankan mendapatkan perhatian khusus, seperti mentoring atau bantuan akademik."
            )
        else:
            st.success("✅ Low Risk")
            st.write("Mahasiswa menunjukkan performa yang stabil.")

        st.info(f"📊 Dropout Probability: {proba:.2%}")

    except Exception as e:
        st.error(f"Error during prediction: {e}")

# ======================
# FOOTER
# ======================

st.markdown("---")
st.caption("Built with Streamlit | Data Science Project")
