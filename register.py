import streamlit as st
import pandas as pd
import os

st.title("🔐 Register")

username = st.text_input("👤 Username")
email = st.text_input("📧 Email")
password = st.text_input("🔑 Password", type="password")
confirm_password = st.text_input("🔁 Confirm Password", type="password")

if st.button("Register"):
    if not username or not email or not password:
        st.warning("Please fill all fields.")
    elif password != confirm_password:
        st.error("Passwords do not match.")
    else:
        file_path = "users.csv"
        if os.path.exists(file_path):
            users = pd.read_csv(file_path)
            if username in users["username"].values:
                st.error("Username already exists.")
            else:
                new_user = pd.DataFrame([[username, password, email]], columns=["username", "password", "email"])
                new_user.to_csv(file_path, mode='a', header=False, index=False)
                st.success("✅ Registration successful. You can now log in.")
        else:
            new_user = pd.DataFrame([[username, password, email]], columns=["username", "password", "email"])
            new_user.to_csv(file_path, index=False)
            st.success("✅ Registration successful. You can now log in.")
