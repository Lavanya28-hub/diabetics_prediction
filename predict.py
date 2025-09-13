import streamlit as st
import numpy as np
import pickle
import io

# Load model
model = pickle.load(open("diabetes_model.pkl", "rb"))

# --- Health insight functions ---
def bmi_category(value):
    if value < 18.5:
        return "🔵 Underweight"
    elif 18.5 <= value < 25:
        return "🟢 Normal"
    elif 25 <= value < 30:
        return "🟠 Overweight"
    else:
        return "🔴 Obese"

def bp_status(value):
    if value < 60:
        return "🔵 Low BP"
    elif 60 <= value <= 90:
        return "🟢 Normal BP"
    else:
        return "🔴 High BP"

def dpf_risk(value):
    if value < 0.5:
        return "🟢 Low hereditary risk"
    elif value < 1.0:
        return "🟠 Moderate hereditary risk"
    else:
        return "🔴 High hereditary risk"

# --- UI Layout ---import streamlit as st

st.title("Diabetes Prediction System")

glucose = st.number_input("Glucose Level", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=0)

if st.button("🔍 Predict"):
    input_data = np.array([[glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)[0]

    # ✅ Prediction result
    st.subheader("🧪 Result:")
    st.success("✅ You are **Not Diabetic**" if prediction == 0 else "⚠️ You are **Diabetic**")

    # ✅ Health insights
    st.subheader("📋 Health Insight:")
    st.markdown(f"**BMI Status:** {bmi_category(bmi)}")
    st.markdown(f"**Blood Pressure:** {bp_status(bp)}")
    st.markdown(f"**Genetic Risk (DPF):** {dpf_risk(dpf)}")

    # ✅ Doctor recommendation
    st.subheader("🩺 Doctor's Note (Suggestion):")
    if prediction == 1:
        st.markdown("""
        - Please consult a diabetologist for a full diagnosis.
        - Maintain a healthy diet and monitor blood sugar levels.
        - Consider regular exercise and reducing BMI if applicable.
        """)
    else:
        st.markdown("""
        - Maintain a balanced diet and active lifestyle.
        - Schedule regular check-ups to stay safe.
        - Keep an eye on glucose and BP levels over time.
        """)

    import pandas as pd
import os
from datetime import datetime

# Save result if user is logged in
if "user" in st.session_state:
    user = st.session_state["user"]
    data = {
        "username": user,
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Glucose": glucose,
        "BloodPressure": bp,
        "SkinThickness": skin,
        "Insulin": insulin,
        "BMI": bmi,
        "DPF": dpf,
        "Age": age,
        "Result": "Diabetic" if prediction == 1 else "Not Diabetic"
    }
    file_exists = os.path.exists("predictions.csv")
    df = pd.DataFrame([data])
    df.to_csv("predictions.csv", mode='a', header=not file_exists, index=False)


    # ✅ Report download code (place here)
    import io

    report = f"""
Diabetes Prediction Result: {'Diabetic' if prediction == 1 else 'Not Diabetic'}

🧪 Your Inputs:
Glucose: {glucose}
Blood Pressure: {bp} ({bp_status(bp)})
Skin Thickness: {skin}
Insulin: {insulin}
BMI: {bmi} ({bmi_category(bmi)})
DPF: {dpf} ({dpf_risk(dpf)})
Age: {age}

🩺 Doctor Recommendation:
{"Consult a diabetologist and monitor regularly." if prediction == 1 else "Maintain healthy lifestyle and monitor periodically."}
"""

    report_bytes = io.BytesIO()
    report_bytes.write(report.encode('utf-8'))
    report_bytes.seek(0)

    st.download_button(
        label="📥 Download Report (.txt)",
        data=report_bytes,
        file_name="diabetes_report.txt",
        mime="text/plain"
    )
