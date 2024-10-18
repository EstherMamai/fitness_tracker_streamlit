# Health and Fitness Tracker

A simple yet powerful web application to help users track their daily fitness data such as steps, weight, activity, and calorie intake. The application also calculates calories burned based on user input and provides insights into their calorie balance (deficit or surplus). This project is built using Streamlit and designed for ease of use.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Features
- **Login/Logout System**: Allows users to securely log in to their account and track their fitness progress.
- **Steps Tracking**: Input daily steps, weight, and duration of physical activities such as walking, running, cycling, and swimming.
- **Calories Calculations**: Automatically calculates calories burned based on steps taken and activity performed.
- **Meals Tracking**: Users can log their meals and track the number of calories consumed.
- **Calorie Balance**: The app calculates if the user is in a calorie surplus or deficit for the day.
- **Data Visualization**: Displays daily fitness data in a table, showing steps, calories burned, calories consumed, and more.
- **Settings**: Customize app settings (e.g., updating personal preferences).

## Installation
To run this project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/EstherMamai/health-and-fitness-tracker.git
   ```
   
2. **Navigate to the Project Directory**
   ```bash
   cd health-and-fitness-tracker
   ```

3. **Create a Virtual Environment (optional but recommended)**
   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## Usage

### 1. **Login**
   - Open the web app in your browser.
   - On the login page, enter your username and password. The default login credentials are `admin` for username and `password` for the password (this should be updated for production use).
   - After successful login, you will be redirected to the **Home** page.

### 2. **Tracking Your Fitness Data**
   - **Input Steps and Activity**: On the sidebar, enter your steps, weight, and duration of any physical activity.
   - **Add Meals**: Log your meals along with the calories consumed.
   - **View Fitness Data**: After submitting your data, you will see a table of your fitness data and an analysis of your calorie balance.

### 3. **Navigation**
   - Use the sidebar to navigate between different sections like Home, Settings, and Logout.


## Technologies Used
- **Streamlit**: The main framework used for building the web app.
- **Pandas**: For data handling and storage.
- **Matplotlib**: For data visualization.
- **Python**: The programming language used.

## Contributing
Contributions are welcome! If you'd like to improve the app or fix any issues, feel free to open a pull request. Before submitting your contributions, make sure to:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a pull request on GitHub.
