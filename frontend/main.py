import streamlit as st
import requests

# 認証状態を保持
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.title("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        response = requests.post(
            "http://backend:8000/auth/login",
            json={"username": username, "password": password}
        )
        if response.status_code == 200:
            st.session_state["logged_in"] = True
            st.success("Logged in successfully")
        else:
            st.error("Invalid username or password")
else:
    st.title("Welcome!")
    st.write("You are logged in.")
    if st.button("Logout"):
        st.session_state["logged_in"] = False
