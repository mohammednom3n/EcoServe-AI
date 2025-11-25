import pandas as pd
import numpy as np
from pathlib import Path

# 1) LOAD DATA

proj_root = Path(__file__).resolve().parent.parent
path = proj_root / "data" / "raw" / "train.csv" 

df = pd.read_csv(path)


# 2) Pre-Pipeline Manual Cleaning


df.drop(columns = ['ID'], inplace = True)

cat_cols = df.select_dtypes(include = "object").columns
for col in cat_cols:
    df[col] = df[col].str.lower().str.strip()

# Fill null values
df['staff_experience'].fillna('unknown', inplace = True)

# Extract Features from date
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['is_weekend'] = (df['date'].dt.weekday >= 5).astype(int)
df.drop(columns = ['date'], inplace = True)


# 3) Define Target and Features

X = df.drop(columns = ['food_waste_kg'])
y = df['food_waste_kg']

# Split the dataset

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.2, random_state = 42)

# 4) Building a pipeline:

# we have to treat features differently
categorical_cols = ['staff_experience', 'waste_category']
numerical_cols = [ col for col in X_train.columns if col not in categorical_cols]

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# Encoding only categorical columns
preprocess = ColumnTransformer(
    transformers= [
        ("cat", OrdinalEncoder(), categorical_cols),
    ],

    remainder= "passthrough"

)

# Full Pipeline: Preprocess + model

model_pipeline = Pipeline(steps=[
    ("preprocessor", preprocess),
    ("model", RandomForestRegressor(
        n_estimators= 300,
        random_state= 42,
        max_depth= 15
    ))
])


# 5) Train model

model_pipeline.fit(X_train, y_train)


# 6) Evaluate model

from sklearn.metrics import mean_absolute_error, r2_score

preds = model_pipeline.predict(X_test)

print("MAE:", mean_absolute_error(y_test, preds))
print("R2:", r2_score(y_test, preds))


# 7) Save model

import joblib

model_dir = proj_root / "models"
model_dir.mkdir(exist_ok = True)

model_path = model_dir / "ecoserve_model.pkl"
joblib.dump(model_pipeline, model_path)

print(f"Model saved to: {model_path}")

