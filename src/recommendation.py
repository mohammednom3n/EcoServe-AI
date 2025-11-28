def make_recommendation(

  predicted_waste_kg: float,
  planned_meals: int | None = None,
  avg_meal_weight_kg: float = 0.8,
  emission_factor: float = 2.5,
  waste_threshold: float = 0.1  # 10% waste tolerance


):
    
    waste_kg = max(predicted_waste_kg, 0.0)
    co2_kg = waste_kg * emission_factor

    result = {
        "predicted_waste_kg": round(waste_kg, 1),
        "estimated_co2_emission": round(co2_kg, 2),
        "waste_percent": None,
        "suggested_meals": None,
        "message": "",

    }

    if planned_meals is not None and planned_meals > 0:
        total_food_kg = planned_meals * avg_meal_weight_kg
        waste_percent = waste_kg / total_food_kg
        result["waste_percent"] = round(waste_percent * 100, 1)

        if waste_percent > waste_threshold:
            reduction_factor = 1 - (waste_percent - waste_threshold)
            suggested_meals = reduction_factor * planned_meals
            result["suggested_meals"] = suggested_meals
            result["message"] = (
                f"Predicted waste is high: {result['waste_percent']}\n"
                f"Consider reducing meals from {planned_meals} to {int(result['suggested_meals'])}"
            ) 
        
        else:
            result["suggested_meals"] = planned_meals
            result["message"] = (
                f"Predicted waste is within the target threshold: {result['waste_percent']}\n"
                f"Current plan of {planned_meals} looks acceptable"
            )

    else:
        result["message"] = (
                f"Predicted waste is: {result['waste_percent']}\n"
                f"Provide a planned_meals value to get a concrete meal preparation recommendation"
            )    
        

    return result
