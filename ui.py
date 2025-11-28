# import streamlit as st
# import requests

# # ----------------------------
# # CONFIG
# # ----------------------------
# API_URL = "https://ecoserve-ai.onrender.com/predict"

# st.set_page_config(
#     page_title="EcoServe-AI Dashboard",
#     page_icon="🌱",
#     layout="centered"
# )

# st.title("🌱 EcoServe-AI")
# st.subheader("Smart Food Waste Forecasting & Sustainability Assistant")
# st.write("Enter tomorrow's planned conditions to estimate waste, CO₂, and optimal meal preparation.")

# # ----------------------------
# # INPUT FORM
# # ----------------------------

# with st.form("input_form"):
#     st.write("### 🍽️ Meal & Operations")

#     meals_served = st.number_input("Planned meals for tomorrow", min_value=1, value=500)
#     kitchen_staff = st.number_input("Kitchen staff count", min_value=1, value=10)
#     staff_experience = st.selectbox("Staff Experience Level", ["beginner", "intermediate", "expert"])
    
#     st.write("### 🌦️ Weather")
#     temperature_C = st.number_input("Temperature (°C)", value=30.0)
#     humidity_percent = st.number_input("Humidity (%)", value=50.0)

#     st.write("### 📅 Day & Events")
#     day_of_week = st.selectbox("Day of Week (0=Mon ... 6=Sun)", list(range(7)))
#     month = st.selectbox("Month", list(range(1, 13)))
#     is_weekend = st.selectbox("Weekend?", [0, 1])
#     special_event = st.selectbox("Special Event?", [0, 1])

#     st.write("### ♻️ Waste History")
#     past_waste_kg = st.number_input("Yesterday’s Waste (kg)", value=20.0)
#     waste_category = st.selectbox("Waste Category", ["meat", "veggivegetables", "dairy", "grains"])

#     submitted = st.form_submit_button("Predict Waste")

# # ----------------------------
# # API CALL
# # ----------------------------
# if submitted:
#     with st.spinner("Analyzing..."):
#         payload = {
#             "meals_served": meals_served,
#             "kitchen_staff": kitchen_staff,
#             "temperature_C": temperature_C,
#             "humidity_percent": humidity_percent,
#             "day_of_week": day_of_week,
#             "special_event": special_event,
#             "past_waste_kg": past_waste_kg,
#             "staff_experience": staff_experience,
#             "waste_category": waste_category,
#             "month": month,
#             "is_weekend": is_weekend,
#         }

#         try:
#             resp = requests.post(API_URL, json=payload)
#             result = resp.json()

#             st.success("Prediction Complete!")

#             # ----------------------------
#             # OUTPUT DISPLAY
#             # ----------------------------
#             st.write("## 📊 Results")
#             st.metric("Predicted Waste (kg)", f"{result['predicted_waste_kg']} kg")
#             st.metric("Estimated CO₂ Emission", f"{result['estimated_co2_emission']} kg")
#             st.metric("Waste Percentage", f"{result['waste_percent']}%")

#             st.write("### 🛠 Recommended Meals")
#             st.metric("Suggested Meals", int(result["suggested_meals"]))

#             st.write("### 💬 Recommendation")
#             st.info(result["message"])

#         except Exception as e:
#             st.error("Something went wrong connecting to the API.")
#             st.error(str(e))

###############################################
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# ----------------------------
# CONFIG
# ----------------------------
API_URL = "https://ecoserve-ai.onrender.com/predict"

st.set_page_config(
    page_title="EcoServe-AI Dashboard",
    page_icon="🌱",
    layout="centered"
)

# ----------------------------
# HEADER WITH IMAGE (Optional)
# ----------------------------
st.markdown(
    """
    <h1 style='text-align:center; color:#2e7d32;'>
        🌱 EcoServe-AI
    </h1>
    <h3 style='text-align:center; color:#4caf50;'>
        Smart Food Waste Forecasting & Sustainability Assistant
    </h3>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.write("Enter tomorrow's planned conditions to estimate waste, CO₂ impact, and receive eco-friendly meal preparation advice.")

# ----------------------------
# INPUT FORM
# ----------------------------
with st.form("input_form"):
    st.markdown("## 🍽️ Meal & Operations")

    col1, col2, col3 = st.columns(3)
    with col1:
        meals_served = st.number_input("Planned meals for tomorrow", min_value=1, value=500)
    with col2:
        kitchen_staff = st.number_input("Kitchen staff count", min_value=1, value=10)
    with col3:
        staff_experience = st.selectbox("Staff Experience Level", ["beginner", "intermediate", "expert"])
        

    st.markdown("## 🌦️ Weather")
    col4, col5 = st.columns(2)
    with col4:
        temperature_C = st.number_input("Temperature (°C)", value=30.0)
    with col5:
        humidity_percent = st.number_input("Humidity (%)", value=50.0)

    st.markdown("## 📅 Day & Events")
    day_of_week = st.selectbox("Day of Week (0=Mon ... 6=Sun)", list(range(7)))
    month = st.selectbox("Month", list(range(1, 13)))
    is_weekend = st.radio("Weekend?", [0, 1], horizontal=True)
    special_event = st.radio("Special Event?", [0, 1], horizontal=True)

    st.markdown("## ♻️ Waste History")
    past_waste_kg = st.number_input("Yesterday’s Waste (kg)", value=20.0)
    waste_category = st.selectbox("Waste Category", ["meat", "vegetables", "dairy", "grains"])

    submitted = st.form_submit_button("🌱 Predict Waste", use_container_width=True)

# ----------------------------
# API CALL
# ----------------------------
if submitted:
    with st.spinner("Analyzing sustainability impact... 🌍"):
        payload = {
            "meals_served": meals_served,
            "kitchen_staff": kitchen_staff,
            "temperature_C": temperature_C,
            "humidity_percent": humidity_percent,
            "day_of_week": day_of_week,
            "special_event": special_event,
            "past_waste_kg": past_waste_kg,
            "staff_experience": staff_experience,
            "waste_category": waste_category,
            "month": month,
            "is_weekend": is_weekend,
        }

        try:
            resp = requests.post(API_URL, json=payload)
            result = resp.json()

            st.success("Prediction Complete! 🌱")

            # ----------------------------
            # OUTPUT DISPLAY
            # ----------------------------
            st.markdown("## 📊 Sustainability Results")

            colA, colB, colC = st.columns(3)
            colA.metric("🥡 Predicted Waste", f"{result['predicted_waste_kg']} kg")
            colB.metric("🌍 CO₂ Emission", f"{result['estimated_co2_emission']} kg")
            colC.metric("📉 Waste Percentage", f"{result['waste_percent']}%")

            st.markdown("### 🥗 Recommended Meal Preparation")
            st.metric("Suggested Meals", int(result["suggested_meals"]))

            st.markdown("### 💬 Recommendation Summary")
            st.info(result["message"])

            # Eco style separator
            st.markdown(
                "<hr style='border:1px solid #4caf50'>",
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error("❌ Something went wrong connecting to the API.")
            st.code(str(e))