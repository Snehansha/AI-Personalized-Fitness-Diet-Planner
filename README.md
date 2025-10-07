A smart, interactive Streamlit app that generates customized workout and meal plans based on user preferences, goals, and body metrics. This app provides practical, AI-driven guidance to help students and fitness enthusiasts achieve their health goals.

Features

Personalized Workout Plan: Generates exercises tailored to your fitness level, goal (weight loss, muscle gain, maintenance), and available equipment.

Personalized Meal Plan: Filters meals based on preferred cuisine, dietary choice (Vegetarian / Non-Veg), and nutritional requirements.

BMI & Health Metrics: Calculates BMI and provides insights for ideal weight range and daily calorie recommendations.

Interactive Dashboard: Expander UI for daily workout and meal plan details.

Nutritional Overview: Visual summary of calories, protein, carbs, and fats.

Advanced Options: Users can specify gender, age, height, weight, and dietary preferences.

Installation

Clone the repository:

git clone https://github.com/your-username/ai-fitness-diet-planner.git
cd ai-fitness-diet-planner


Create a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows:

.\venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

Usage

Run the Streamlit app:

streamlit run app.py


Select your gender, age, weight, height, and fitness goal in the sidebar.

Choose your equipment availability and preferred cuisine/diet.

Click Generate My Plan to get your personalized workout and meal plan.

View your weekly plan, nutritional summary, and daily exercise details.

Future Enhancements

Export plan as PDF or CSV.

Weekly calendar view for workouts & meals.

Motivational badges & streak tracking.

AI-generated tips for daily workouts and nutrition.

Tech Stack

Python

Streamlit

Pandas

Altair / Plotly (optional for charts)

License

MIT License © 2025 Snehansha Das
