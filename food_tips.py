import streamlit as st

st.title("🥗 Food Habits & Tips")

bmi = st.slider("Your BMI", 10.0, 50.0, 25.0)
diabetic = st.radio("Are you diabetic?", ["Yes", "No"])

if diabetic == "Yes":
    st.warning("Avoid high-sugar and high-carb foods.")
    st.markdown("""
    - Eat more fiber-rich foods (e.g., vegetables, legumes)
    - Include whole grains (brown rice, oats)
    - Stay hydrated and avoid sugary drinks
    """)
else:
    st.success("Maintain a balanced diet to prevent diabetes.")
    st.markdown("""
    - Fruits, vegetables, lean protein
    - Moderate carbs and sugar intake
    """)

if bmi >= 30:
    st.error("You're in the **Obese** range. Consider weight management.")
elif bmi >= 25:
    st.warning("You're **Overweight**. Consider physical activity.")
else:
    st.success("Your BMI is in the **Healthy** range!")
