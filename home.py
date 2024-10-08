import streamlit as st

# Function for home page
def home_page():
    st.title(f"Home - Welcome {st.session_state.current_user}")
    user_email = st.session_state.users[st.session_state.current_user]["email"]
    st.write(f"Email: {user_email}")
    
    # Placeholder for the fitness tracker functionality
    st.write("This is your fitness tracker dashboard!")
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.session_state.page = "login"  # Redirect to login after logout