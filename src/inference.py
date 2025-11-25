import joblib
from pathlib import Path
import pandas as pd

proj_root = Path(__file__).resolve().parent.parent
model_path = proj_root / "models" / "ecoserve_model.pkl"

model = joblib.load(model_path)

def predict_waste(input_data: dict):

    df = pd.DataFrame([input_data])
    waste_kg = model.predict(df)[0]
    return float(waste_kg)
