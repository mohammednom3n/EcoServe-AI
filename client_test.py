import requests

URL = "https://ecoserve-ai.onrender.com/predict"  # change this

payload = {
    "meals_served": 550,
    "kitchen_staff": 10,
    "temperature_C": 30.0,
    "humidity_percent": 50.0,
    "day_of_week": 1,
    "special_event": 0,
    "past_waste_kg": 40.0,
    "staff_experience": "beginner",
    "waste_category": "vegetables",
    "month": 1,
    "is_weekend": 0,
}

resp = requests.post(URL, json=payload)
print("Status:", resp.status_code)
print("Response:", resp.json())
