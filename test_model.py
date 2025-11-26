from src.inference import predict_waste
from src.recommendation import make_recommendation

sample = {
    "meals_served": 350,
    "kitchen_staff": 6,
    "temperature_C": 24,
    "humidity_percent": 85,
    "day_of_week": 1,
    "special_event": 0,
    "past_waste_kg": 30,
    "staff_experience": "beginner",
    "waste_category": "grains",
    "month": 7,
    "is_weekend": 0,
}
waste_kg = predict_waste(sample)

print(make_recommendation(
    predicted_waste_kg= waste_kg,
    planned_meals= sample["meals_served"]
)
)