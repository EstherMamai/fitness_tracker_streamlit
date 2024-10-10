import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Initialize session state for navigation and user authentication
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'users' not in st.session_state:
    st.session_state.users = {}
if 'meals' not in st.session_state:
    st.session_state.meals = []
if 'total_calories_consumed' not in st.session_state:
    st.session_state.total_calories_consumed = 0
if 'fitness_data' not in st.session_state:
    st.session_state.fitness_data = pd.DataFrame(columns=['Date', 'Steps', 'Calories from Steps', 'Calories from Activity', 'Total Calories Burned', 'Total Calories Consumed', 'Calories Balance'])

# Function to handle login
def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Here you would validate the user credentials
        if username == "admin" and password == "password":  # Example login validation
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.success("Successfully logged in!")
            st.session_state.page = "Home"
        else:
            st.error("Invalid username or password.")

# Home page function
def home_page():
    if not st.session_state.logged_in:
        st.error("You need to be logged in to access this page.")
        return

    st.title(f"Home - Welcome {st.session_state.current_user}")
    user_email = st.session_state.users.get(st.session_state.current_user, {}).get("email", "Not found")
    st.write(f"Email: {user_email}")

    # Title of the app
    st.title('Health and Fitness Tracker')

    # Sidebar inputs for user's fitness data
    st.sidebar.header('Input Your Daily Fitness Data')

    steps = st.sidebar.number_input('Enter your steps for today', min_value=0)
    weight = st.sidebar.number_input('Enter your weight (kg)', min_value=0.0, step=0.1)
    activity = st.sidebar.selectbox("Choose a physical activity", ["None", "Walking", "Running", "Cycling", "Swimming"])
    activity_duration = st.sidebar.number_input("Enter duration of activity (hours)", min_value=0.0, step=0.1)
    
    # Date input
    date = st.sidebar.date_input('Date', datetime.date.today())

    # Function to calculate calories burned from steps
    def calculate_calories_from_steps(steps, weight):
        calories_per_step = weight / 20  # Rough estimate
        return steps * calories_per_step

    # Function to calculate calories burned from activity
    def calculate_calories_from_activity(activity, weight, duration):
        met_values = {
            "Walking": 3.5,
            "Running": 8.3,
            "Cycling": 7.5,
            "Swimming": 9.8
        }
        if activity == "None":
            return 0
        return met_values[activity] * weight * duration

    # Calculate calories burned
    calories_burned_from_steps = calculate_calories_from_steps(steps, weight)
    calories_from_activity = calculate_calories_from_activity(activity, weight, activity_duration)
    total_calories_burned = calories_burned_from_steps + calories_from_activity

    # Section for calories consumed by meals
    st.sidebar.header('Calories Consumed by Meals')
    meal_name = st.sidebar.text_input('Meal Name')
    meal_calories = st.sidebar.number_input('Calories for this meal', min_value=0)

    if st.sidebar.button('Add Meal'):
        if meal_name and meal_calories > 0:
            st.session_state.meals.append({'meal': meal_name, 'calories': meal_calories})
            st.session_state.total_calories_consumed += meal_calories
            st.sidebar.success(f'Added {meal_name} with {meal_calories} calories.')
        else:
            st.sidebar.warning("Please enter a valid meal name and calories.")

    # Display the list of meals and total calories
    st.sidebar.subheader('Meals Entered:')
    if st.session_state.meals:
        for meal in st.session_state.meals:
            st.sidebar.write(f"{meal['meal']}: {meal['calories']} calories")
        st.sidebar.write(f"Total Calories Consumed: {st.session_state.total_calories_consumed}")

    # Calories balance
    calories_balance = st.session_state.total_calories_consumed - total_calories_burned
    st.subheader('Calories Balance')
    if calories_balance > 0:
        st.write(f"Surplus! You have consumed {calories_balance} more calories than you burned today.")
    elif calories_balance < 0:
        st.write(f"Deficit! You have burned {-calories_balance} more calories than you consumed today.")
    else:
        st.write("You have perfectly balanced your calories today.")

    # Data storage and visualization
    if st.sidebar.button('Add Data'):
        new_data = pd.DataFrame({
            'Date': [date],
            'Steps': [steps],
            'Calories from Steps': [calories_burned_from_steps],
            'Calories from Activity': [calories_from_activity],
            'Total Calories Burned': [total_calories_burned],
            'Total Calories Consumed': [st.session_state.total_calories_consumed],
            'Calories Balance': [calories_balance],
        })
        st.session_state.fitness_data = pd.concat([st.session_state.fitness_data, new_data], ignore_index=True)
        st.success('Data added successfully!')

    st.subheader('Your Fitness Data')
    st.write(st.session_state.fitness_data)

# Settings page function
def settings_page():
    st.title("Settings Page")
    st.write("This is where you can update your app preferences.")

# Logout function
def logout():
    st.session_state.logged_in = False
    st.session_state.current_user = None
    st.session_state.page = "login"
    st.success("You have been logged out.")

# Navigation bar
def navigation():
    if not st.session_state.logged_in:
        login()
    else:
        st.sidebar.title("Navigation")
        selected_page = st.sidebar.radio("Go to", ["Home", "Settings", "Logout"])
        if selected_page == "Home":
            st.session_state.page = "Home"
        elif selected_page == "Settings":
            st.session_state.page = "Settings"
        elif selected_page == "Logout":
            logout()

# Main page display
def main():
    navigation()  # Call the navigation bar

    if st.session_state.page == "Home":
        home_page()
    elif st.session_state.page == "Settings":
        settings_page()

if __name__ == "__main__":
    main()