import streamlit as st
import pandas as pd

st.title("📊 Your Prediction History")

if "user" in st.session_state:
    user = st.session_state["user"]
    try:
        df = pd.read_csv("predictions.csv")
        user_history = df[df["username"] == user]
        if not user_history.empty:
            st.dataframe(user_history.sort_values("date_time", ascending=False))
        else:
            st.info("No predictions found for your account.")
    except FileNotFoundError:
        st.warning("No prediction records yet.")
else:
    st.warning("Please log in to view your prediction history.")
