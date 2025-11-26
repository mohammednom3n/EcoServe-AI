from src.inference import predict_waste
from src.recommendation import make_recommendation

sample = {
    "meals_served": 460,
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
}
waste_kg = predict_waste(sample)

print(make_recommendation(
    predicted_waste_kg= waste_kg,
    planned_meals= sample["meals_served"]
)
)