import streamlit as st
import pandas as pd

st.title("🔓 Login")

username = st.text_input("👤 Username")
password = st.text_input("🔑 Password", type="password")

if st.button("Login"):
    try:
        users = pd.read_csv("users.csv", usecols=["username", "password"])

        user_row = users[(users["username"] == username) & (users["password"] == password)]
        if not user_row.empty:
            st.success(f"✅ Welcome, {username}!")
            st.session_state["user"] = username
            st.switch_page("pages/about.py")  # Redirect to about page
        else:
            st.error("❌ Invalid credentials.")
    except FileNotFoundError:
        st.error("User database not found. Please register first.")
