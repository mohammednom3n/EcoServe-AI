from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from src.inference import predict_waste
from src.recommendation import make_recommendation

app = FastAPI(title="EcoServe-AI API")

class PredictionRequest(BaseModel):
    meals_served: int
    kitchen_staff: int
    temperature_C: float
    humidity_percent: float
    day_of_week: int
    special_event: int
    past_waste_kg: float
    staff_experience: str
    waste_category: str
    month: int
    is_weekend: int


@app.post("/predict")
def predict(req: PredictionRequest):
    data = req.dict()
    planned_meals = data["meals_served"]

    waste_kg = predict_waste(data)
    
    rec = make_recommendation(waste_kg, planned_meals)

    return rec