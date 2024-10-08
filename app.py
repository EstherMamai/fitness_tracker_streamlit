import streamlit as st
from auth import login_page, sign_up_page
from home import home_page

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