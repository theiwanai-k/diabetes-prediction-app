import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model1.pkl", "rb") as f:
    model1 = pickle.load(f)

st.title("Diabetes Prediction System 🩺")

st.subheader("Enter Patient Details")break

# Pregnancies: dropdown (0–10 + 'More than 10')
pregnancy_options = list(range(0, 11)) + ["More than 10"]
pregnancy_input = st.selectbox("Number of Pregnancies", pregnancy_options)

# Convert "More than 10" to 11 for model
if pregnancy_input == "More than 10":
    pregnancies = 11
else:
    pregnancies = pregnancy_input

# Glucose input
glucose = st.number_input("Glucose Level", min_value=0, max_value=1000, value=120)

# Blood Pressure input
bp = st.number_input("Blood Pressure", min_value=0, max_value=1000, value=70)

# BMI input
bmi = st.number_input("BMI", min_value=0.0, max_value=1000.0, value=25.0)

# Diabetes Pedigree Function input
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=1000.0, value=0.5)

# Age input
age = st.number_input("Age", min_value=1, max_value=120, value=30)

# Race: dropdown (Black, Hispanic, White)
race_dict = {'Black': 0, 'Hispanic': 1, 'White': 2}
race_input = st.selectbox("Race", list(race_dict.keys()))
race = race_dict[race_input]

# Collect all features in order
features = np.array([[pregnancies, glucose, bp, bmi, dpf, age, race]])

# Prediction
if st.button("Predict"):
    prediction = model1.predict(features)[0]

    if prediction == 0:
        st.success("No diabetic symptoms ✅")
    else:
        st.error("⚠️ You have possibilities of diabetes. Please consult a doctor.")