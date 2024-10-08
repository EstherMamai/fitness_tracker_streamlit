i# home.py
import streamlit as st

# Function for home page
def home_page():
    st.title(f"Home - Welcome {st.session_state.current_user}")
    
    user_email = st.session_state.users[st.session_state.current_user]["email"]
    st.write(f"Email: {user_email}")
    
    # Logout button styled and positioned at the top right
    logout_button = """
    <style>
    .logout-button {
        position: absolute;
        top: 10px;
        right: 10px;
        background-color: #007BFF; /* Blue color */
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        border-radius: 5px;
    }
    </style>
    <button class="logout-button" onclick="document.getElementById('logout').click()">Logout</button>
    <input type="button" id="logout" style="display:none;" onclick="logout()" />
    <script>
    function logout() {
        window.location.reload(); // Refresh page to trigger logout
    }
    </script>
    """
    
    # Display the logout button using HTML
    st.markdown(logout_button, unsafe_allow_html=True)
    
    # Placeholder for the fitness tracker functionality
    st.write("This is your fitness tracker dashboard!")

    # Handle logout
    if st.button("Logout", key='logout'):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.session_state.page = "login"  # Redirect to login after logout
