import requests

URL = "https://ecoserve-ai.onrender.com/predict"  # change this

payload = {
    "meals_served": 500,
    "kitchen_staff": 12,
    "temperature_C": 30.0,
    "humidity_percent": 60.0,
    "day_of_week": 2,
    "special_event": 0,
    "past_waste_kg": 40.0,
    "staff_experience": "intermediate",
    "waste_category": "meat",
    "month": 9,
    "is_weekend": 0,
    "planned_meals": 550
}

resp = requests.post(URL, json=payload)
print("Status:", resp.status_code)
print("Response:", resp.json())
