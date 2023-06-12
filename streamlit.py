import streamlit as st
import requests

API_URL = 'http://localhost:8000/api/'  # Replace with your API URL

def register_user(username, password, email):
    response = requests.post(API_URL + 'register/', data={'username': username, 'password': password, 'email': email})
    return response.json()

def login_user(username, password):
    response = requests.post(API_URL + 'login/', data={'username': username, 'password': password})
    return response.json()

def logout_user():
    response = requests.get(API_URL + 'logout/')
    return response.json()

def main():
    st.title("Django Authentication with Streamlit")
    st.write("Welcome to the Django Authentication with Streamlit app!")

    # Registration
    st.subheader("Register")
    reg_username = st.text_input("Username:")
    reg_password = st.text_input("Password:", type="password")
    reg_email = st.text_input("Email:")
    if st.button("Register"):
        response = register_user(reg_username, reg_password, reg_email)
        if 'error' in response:
            st.error(response['error'])
        else:
            st.success(response['success'])
        st.text_input("")

    #
