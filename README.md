# EcoServe-AI🌱 **(Smart Food Waste Forecasting System)**

A data-driven system that helps cafeterias **cook the right amount of food** by
**predicting meal demand** and **estimating waste & CO₂ emissions**, then offering
a smarter meal preparation recommendation.

---

## 🎯 Problem Overview

Cafeterias in universities, hospitals, and corporate offices often **cook more food than needed**
because it is difficult to predict how many people will eat each day.
Attendance changes due to:

- Weather conditions
- Weekday vs. weekend patterns
- Exams or special events
- Seasonal changes

This leads to:

- 🍱 **Food waste**
- 💸 **Unnecessary operational costs**
- 🌍 **Higher CO₂ emissions** from producing food that is not consumed

**Example: GreenBite University Cafeteria**

- Prepares **500–600 meals per day**
- Records **15–25% leftovers**
- Wastes **60–80 kg of food per month**
- Generates **~150–200 kg of CO₂ emissions from waste**

---

## 🧠 Solution Summary

The system uses **Machine Learning to forecast daily meal demand** (meals likely to be eaten tomorrow).  
Then it evaluates the cafeteria’s **planned meal preparation** and provides:

- 📌 **Waste estimation (in kg)**
- ♻️ **CO₂ emission estimation**
- 🧾 **Recommended number of meals to cook** (slightly above demand using a small safety margin)

### 🔍 Key Insight

> **We predict how many meals will be eaten.  
> We do NOT predict the planned amount to be cooked.  
> We only recommend how to adjust it.**

---

## 📌 System Workflow

### 🧑‍🍳 User Input
The cafeteria manager enters:

- Date (or “tomorrow”)
- Weather (temperature, humidity)
- Special event? (Yes/No)
- Planned number of meals to cook (optional — default uses prediction only)

### 🤖 Model Prediction (ML)
Predicts:
- **Expected meals to be eaten (demand)**

Example:  
> **480 meals are likely to be eaten**

### 📊 System Calculations (Rules, Not ML)

| Output | How It’s Calculated |
|--------|---------------------|
| **Expected waste (kg)** | `max(planned - predicted, 0) × avg_weight_per_meal` |
| **CO₂ emission (kg)** | `waste_kg × emission_factor` |
| **Recommended meals** | `predicted × (1 + safety_margin)` (never below predicted) |

📌 *Safety margin = 2–5% (configurable)*  
📌 *Emission factor ≈ 3 kg CO₂ per 1 kg waste (can be cited)*  
📌 *Average food weight per meal can be estimated from dataset (≈ 0.8–1 kg per meal)*

### 💡 Example Output

> **Expected demand:** 480 meals  
> **Your plan:** 550 meals  
> **Expected waste:** ≈ 70 meals (≈ 60 kg)  
> **Estimated CO₂:** ≈ 180 kg CO₂  
> **Recommendation:** Prepare **490–500 meals** instead  
> *(Enough for everyone + much less waste)*

---

## 📁 Dataset Description

**File used:** `train.csv`

| Column | Meaning |
|--------|---------|
| `date` | Calendar date |
| `meals_served` | Actual meals eaten (target for ML) |
| `temperature_C` | Average daily temperature |
| `humidity_percent` | Average humidity |
| `day_of_week` | 0 = Monday, 6 = Sunday |
| `special_event` | 0/1 flag |
| `kitchen_staff`, `staff_experience` | Operational features |
| `past_waste_kg` | Previous day’s waste (optional feature) |
| `waste_category` | Type of waste |
| `food_waste_kg` | Actual waste (used for estimating avg weight/meal) |

---

## 🏗️ Project Structure

```bash
smart-food-waste-forecasting/
├── data/
│   └── train.csv
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_Model_Training.ipynb
│   └── 04_Evaluation.ipynb
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── inference.py
│   └── recommendation.py   # Safety margin, waste, CO₂ calculations
├── models/
│   └── demand_model.pkl
├── api/
│   └── main.py             # Flask/FastAPI endpoint
├── README.md
└── requirements.txt
