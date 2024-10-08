import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Title of the app
st.title('Health and Fitness Tracker')

# Sidebar inputs for the user's data
st.sidebar.header('Input Your Daily Fitness Data')

# Input fields for the user
steps = st.sidebar.number_input('Enter your steps for today', min_value=0)
calories_burned_from_steps = 0  # Will be updated by calculation
weight = st.sidebar.number_input('Enter your weight (kg)', min_value=0.0, step=0.1)
activity = st.sidebar.selectbox("Choose a physical activity", ["None", "Walking", "Running", "Cycling", "Swimming"])
activity_duration = st.sidebar.number_input("Enter duration of activity (hours)", min_value=0.0, step=0.1)

calories_from_activity = 0  # Will be updated by calculation

# Date input
date = st.sidebar.date_input('Date', datetime.date.today())

# Function to calculate calories burned from steps
def calculate_calories_from_steps(steps, weight):
    calories_per_step = weight / 20  # Rough estimate: 1 calorie burned per 20 steps per kg
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

# Calculate calories burned from steps
calories_burned_from_steps = calculate_calories_from_steps(steps, weight)
# Calculate calories burned from activity
calories_from_activity = calculate_calories_from_activity(activity, weight, activity_duration)

# Total calories burned
total_calories_burned = calories_burned_from_steps + calories_from_activity

# Section for calories consumed by user-defined meals
st.sidebar.header('Calories Consumed by Meals')

# Initialize or load session state for meals and calories
if 'meals' not in st.session_state:
    st.session_state.meals = []

if 'total_calories_consumed' not in st.session_state:
    st.session_state.total_calories_consumed = 0

# Input fields for the meal name and calories
meal_name = st.sidebar.text_input('Meal Name')
meal_calories = st.sidebar.number_input('Calories for this meal', min_value=0)

# Button to add the meal
if st.sidebar.button('Add Meal'):
    if meal_name and meal_calories > 0:
        st.session_state.meals.append({'meal': meal_name, 'calories': meal_calories})
        st.session_state.total_calories_consumed += meal_calories
        st.sidebar.success(f'Added {meal_name} with {meal_calories} calories.')

# Display the list of meals and total calories
st.sidebar.subheader('Meals Entered:')
if st.session_state.meals:
    for meal in st.session_state.meals:
        st.sidebar.write(f"{meal['meal']}: {meal['calories']} calories")
    st.sidebar.write(f"Total Calories Consumed: {st.session_state.total_calories_consumed}")

# Calories balance (consumed vs burned)
calories_balance = st.session_state.total_calories_consumed - total_calories_burned

# Display calories balance
st.subheader('Calories Balance')
if calories_balance > 0:
    st.write(f"Surplus! You have consumed {calories_balance} more calories than you burned today.")
elif calories_balance < 0:
    st.write(f"Deficit! You have burned {-calories_balance} more calories than you consumed today.")
else:
    st.write("You have perfectly balanced your calories today.")

# Store the inputs in a DataFrame
if 'fitness_data' not in st.session_state:
    st.session_state.fitness_data = pd.DataFrame(columns=['Date', 'Steps', 'Calories from Steps', 'Calories from Activity', 'Total Calories Burned', 'Total Calories Consumed', 'Calories Balance', 'Water'])

if st.sidebar.button('Add Data'):
    # Create a new row with the input data
    new_data = pd.DataFrame({
        'Date': [date],
        'Steps': [steps],
        'Calories from Steps': [calories_burned_from_steps],
        'Calories from Activity': [calories_from_activity],
        'Total Calories Burned': [total_calories_burned],
        'Total Calories Consumed': [st.session_state.total_calories_consumed],
        'Calories Balance': [calories_balance],
        'Water': [st.sidebar.number_input('Enter water intake (liters)', min_value=0.0, step=0.1)]
    })

    # Concatenate the new data with the existing DataFrame
    st.session_state.fitness_data = pd.concat([st.session_state.fitness_data, new_data], ignore_index=True)
    st.success('Data added successfully!')

# Display the stored fitness data
st.subheader('Your Fitness Data')
st.write(st.session_state.fitness_data)

# Visualize progress
if not st.session_state.fitness_data.empty:
    st.subheader('Fitness Progress Over Time')

    fig, ax = plt.subplots(4, 1, figsize=(10, 10))

    # Plot steps
    ax[0].plot(st.session_state.fitness_data['Date'], st.session_state.fitness_data['Steps'], label='Steps', color='blue')
    ax[0].set_title('Steps')
    ax[0].set_xlabel('Date')
    ax[0].set_ylabel('Steps')
    
    # Plot calories from steps
    ax[1].plot(st.session_state.fitness_data['Date'], st.session_state.fitness_data['Calories from Steps'], label='Calories from Steps', color='green')
    ax[1].set_title('Calories Burned from Steps')
    ax[1].set_xlabel('Date')
    ax[1].set_ylabel('Calories')
    
    # Plot calories from activity
    ax[2].plot(st.session_state.fitness_data['Date'], st.session_state.fitness_data['Calories from Activity'], label='Calories from Activity', color='orange')
    ax[2].set_title('Calories Burned from Activity')
    ax[2].set_xlabel('Date')
    ax[2].set_ylabel('Calories')

    # Plot total calories burned
    ax[3].plot(st.session_state.fitness_data['Date'], st.session_state.fitness_data['Total Calories Burned'], label='Total Calories Burned', color='purple')
    ax[3].set_title('Total Calories Burned')
    ax[3].set_xlabel('Date')
    ax[3].set_ylabel('Calories')

    plt.tight_layout()
    st.pyplot(fig)

    # Section for meal plan
st.subheader("Create a Meal Plan")
meal_items = {
    "Eggs (2 large)": 155,
    "Chicken Breast (100g)": 165,
    "Rice (1 cup)": 205,
    "Banana": 105,
    "Salad (1 bowl)": 150,
    "Apple": 95,
    "Avocado (half)": 160,
    "Bread (2 slices)": 133
}

selected_meals = st.multiselect("Select your meal items", list(meal_items.keys()))

if selected_meals:
    total_meal_calories = sum([meal_items[item] for item in selected_meals])
    st.write(f"Total calories for your meal plan: {total_meal_calories} kcal")