import streamlit as st
import pandas as pd

# Initialize session state variables
if 'users' not in st.session_state:
    st.session_state.users = {}  # Dictionary to store users: {username: password}
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

# Function for sign-up
def sign_up_page():
    st.title("Sign Up")
    username = st.text_input("Create a Username")
    password = st.text_input("Create a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    if st.button("Sign Up"):
        if username in st.session_state.users:
            st.error("Username already exists!")
        elif password != confirm_password:
            st.error("Passwords do not match!")
        else:
            st.session_state.users[username] = password
            st.success(f"Account created for {username}! You can now log in.")
            st.session_state.page = "login"  # Redirect to login page

# Function for login
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password.")

# Function for home page
def home_page():
    st.title(f"Home - Welcome {st.session_state.current_user}")
    st.write("This is your fitness tracker dashboard!")

    # Include your existing health and fitness tracker functionality here
    # For now, we just show a placeholder
    st.write("Track your steps, calories, and fitness goals here.")
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.session_state.page = "login"  # Redirect to login after logout

# Logic to show the appropriate page based on login state
if 'page' not in st.session_state:
    st.session_state.page = "login"

if not st.session_state.logged_in:
    if st.session_state.page == "login":
        login_page()
        st.write("Don't have an account? [Sign Up](#)")
        if st.button("Go to Sign Up"):
            st.session_state.page = "signup"
    elif st.session_state.page == "signup":
        sign_up_page()
        st.write("Already have an account? [Login](#)")
        if st.button("Go to Login"):
            st.session_state.page = "login"
else:
    home_page()