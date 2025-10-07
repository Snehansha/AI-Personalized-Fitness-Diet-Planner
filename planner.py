import streamlit as st
import pandas as pd
from pprint import pprint

st.set_page_config(page_title="AI Fitness & Diet Planner", page_icon="💪", layout="wide")

DEFAULT_EXERCISES = {
    "no_equipment": {
        "full_body": [("Push-ups", "3x8-15"), ("Bodyweight Squats", "3x12-20"), ("Plank", "3x30-60s")],
        "cardio": [("Jumping Jacks", "3x60s"), ("High Knees", "3x60s")]
    },
    "basic_gym": {
        "upper": [("Bench Press", "3x8"), ("Shoulder Press", "3x8")],
        "lower": [("Squats", "3x10"), ("Deadlifts", "3x6")],
        "cardio": [("Treadmill", "20 min")]
    }
}

MEALS = [
    {"name": "Oats with Milk", "category": "Breakfast", "cuisine": "Indian", "calories": 250, "protein": 10, "carbs": 35, "fat": 5, "cost": 40, "diet": "Vegetarian"},
    {"name": "Grilled Chicken", "category": "Lunch", "cuisine": "Indian", "calories": 400, "protein": 30, "carbs": 10, "fat": 12, "cost": 100, "diet": "Non-Veg"},
    {"name": "Paneer Salad", "category": "Dinner", "cuisine": "Indian", "calories": 350, "protein": 20, "carbs": 15, "fat": 10, "cost": 80, "diet": "Vegetarian"},
    {"name": "Egg Omelette", "category": "Breakfast", "cuisine": "Continental", "calories": 180, "protein": 12, "carbs": 2, "fat": 10, "cost": 30, "diet": "Non-Veg"},
    {"name": "Rice & Dal", "category": "Lunch", "cuisine": "Indian", "calories": 320, "protein": 12, "carbs": 55, "fat": 4, "cost": 35, "diet": "Vegetarian"}
]

def generate_workout_plan(goal, level, equipment):
    eq = "no_equipment" if equipment in ["none", "minimal"] else "basic_gym"
    plan = []
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for day in days:
        if day in ["Mon","Wed","Fri"]:
            exercises = DEFAULT_EXERCISES[eq]["full_body"] if eq=="no_equipment" else DEFAULT_EXERCISES[eq]["upper"]
        elif day in ["Tue","Thu"]:
            exercises = DEFAULT_EXERCISES[eq]["cardio"]
        else:
            exercises = [("Active Recovery", "30-60 min")]
        plan.append({"day": day, "session": exercises})
    return plan

def generate_meal_plan(cuisine, diet_preference):
    return [meal for meal in MEALS if meal["cuisine"].lower()==cuisine.lower() and (meal["diet"]==diet_preference or diet_preference=="Any")]

def calculate_bmi(weight, height):
    return round(weight / ((height/100)**2), 1)

st.title("💪 AI Personalized Fitness & Diet Planner")
st.write("Create a fully personalized workout and meal plan based on your goals, body stats, and preferences.")

with st.sidebar:
    st.header("Your Details")
    gender = st.selectbox("Gender", ["Male","Female","Other"])
    age = st.number_input("Age", min_value=10, max_value=100, value=25)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
    height = st.number_input("Height (cm)", min_value=120, max_value=230, value=170)
    bmi = calculate_bmi(weight, height)
    st.metric("BMI", bmi)
    
    st.header("Fitness Preferences")
    goal = st.selectbox("Goal", ["Lose Weight","Gain Muscle","Maintain"])
    level = st.selectbox("Fitness Level", ["Beginner","Intermediate","Advanced"])
    equipment = st.selectbox("Equipment", ["None","Basic Gym","Full Gym"])
    cuisine = st.selectbox("Cuisine Preference", ["Indian","Continental"])
    diet_preference = st.selectbox("Diet", ["Vegetarian","Non-Veg","Any"])

if st.button("Generate My Plan"):
    st.subheader("🏋️ Workout Plan")
    workouts = generate_workout_plan(goal, level, equipment)
    for day in workouts:
        with st.expander(f"📅 {day['day']}"):
            for ex, sets in day["session"]:
                st.write(f"- **{ex}** — {sets}")

    st.subheader("🍱 Meal Plan")
    meals = generate_meal_plan(cuisine, diet_preference)
    if meals:
        for meal in meals:
            st.write(f"🍽️ **{meal['category']}**: {meal['name']}")
            st.caption(f"Calories: {meal['calories']} kcal | Protein: {meal['protein']}g | Carbs: {meal['carbs']}g | Fat: {meal['fat']}g | Cost: ₹{meal['cost']}")
    else:
        st.warning("No meals match your preferences!")

    # --- Optional: Summary charts (calories / protein / carbs)
    df = pd.DataFrame(meals)
    if not df.empty:
        st.subheader("📊 Nutritional Overview")
        st.bar_chart(df[["calories","protein","carbs","fat"]])

st.markdown("---")
st.caption("Created by Snehansha Das • Powered by AI 🧠")

