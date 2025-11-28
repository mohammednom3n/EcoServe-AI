from src.inference import predict_waste
from src.recommendation import make_recommendation

sample = {
    "meals_served": 741,
    "kitchen_staff": 10,
    "temperature_C": 30.0,
    "humidity_percent": 50.0,
    "day_of_week": 1,
    "special_event": 0,
    "past_waste_kg": 40,
    "staff_experience": "beginner",
    "waste_category": "vegetables",
    "month": 1,
    "is_weekend": 0,
}
waste_kg = predict_waste(sample)

print(make_recommendation(
    predicted_waste_kg= waste_kg,
    planned_meals= sample["meals_served"]
)
)