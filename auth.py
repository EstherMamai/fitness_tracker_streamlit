import streamlit as st

# Initialize session state variables
if 'users' not in st.session_state:
    st.session_state.users = {}  # Store users as {username: {"password": password, "email": email}}
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

# Function for sign-up
def sign_up_page():
    st.title("Sign Up")
    email = st.text_input("Enter your Email Address")
    username = st.text_input("Create a Username")
    password = st.text_input("Create a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    if st.button("Sign Up"):
        if email == "" or username == "" or password == "":
            st.error("All fields are required!")
        elif username in st.session_state.users:
            st.error("Username already exists!")
        elif password != confirm_password:
            st.error("Passwords do not match!")
        else:
            st.session_state.users[username] = {
                "password": password,
                "email": email
            }
            st.success(f"Account created for {username}! You can now log in.")
            st.session_state.page = "login"  # Redirect to login page

# Function for login
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Invalid username or password.")