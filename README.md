# 🌱 EcoServe-AI  
### Smart Food Waste Forecasting & Sustainability Assistant

EcoServe-AI is a machine learning system that helps institutional cafeterias **reduce food waste before it happens**.  
It predicts **tomorrow’s food waste (in kg)**, converts it to **CO₂ emissions**, and recommends **how much to reduce meal preparation** to minimize waste while still meeting demand.

> 💡 Built for universities, hospitals, and corporate cafeterias that serve hundreds of meals daily.

---

## 📌 Problem Statement

Cafeterias often cook more food than required because daily demand is hard to predict.  
Meal consumption varies based on:

- ⚠️ Weather (temperature, humidity)
- 📅 Day of the week
- 🎉 Events or exams
- 👨‍🍳 Operational factors (staff skill, previous waste)
- 🍽️ Seasonal fluctuations

This leads to:

- 🍱 Significant food waste  
- 💸 Extra kitchen costs  
- 🌍 Higher CO₂ emissions from unused food

### Example: GreenBite University Cafeteria

| Metric | Value |
|--------|------|
| Meals prepared daily | 500–600 |
| Food leftover | 15–25% |
| Monthly waste | 60–80 kg |
| Monthly CO₂ footprint | ~150–200 kg |

---

## 🎯 Project Goal

EcoServe-AI enables cafeterias to:

✔ **Forecast food waste before it occurs**  
✔ **Estimate carbon footprint caused by waste**  
✔ **Receive actionable guidance to reduce meal preparation safely**  

> 🧠 **The model predicts waste directly — not attendance.**  
This provides more accurate sustainability insights and immediately actionable recommendations.

---

## 🔬 How EcoServe-AI Works

### 🔐 Input (from kitchen manager or system)

- 📅 Date (or “tomorrow”)
- 🌡️ Temperature & humidity
- 🎉 Special event? (Yes/No)
- 👨‍🍳 Kitchen staff data (experience level, optional)
- 🍽️ Planned number of meals *(optional)*

### 🤖 Machine Learning Model Output
- **Predicted food waste (kg)**

### 📊 Rule-Based Calculations (Not ML)
| Output | Formula |
|--------|---------|
| CO₂ Emissions | `predicted_waste_kg × emission_factor` |
| Waste % | `predicted_waste_kg / estimated_total_food_kg` |
| Recommended meal adjustment | If waste% > threshold → reduce meals by X% |

📌 Defaults (configurable):  
- Average meal weight: **0.8–1.0 kg per meal**  
- Emission factor: **3 kg CO₂ per 1 kg food waste**  
- Waste tolerance threshold: **10–15%**

---

## 🧾 Example System Output

> 📌 *Your planned meals:* **550**  
> 🔮 *Predicted waste tomorrow:* **60 kg**  
> 🌍 *Estimated CO₂ impact:* **~180 kg CO₂**  
> 🔧 **Recommendation:** Reduce preparation by **10–15%**  
> 🍽️ *Suggested target:* **470–500 meals**  

If no planned meals are entered:

> 🚦 *Predicted waste:* **50 kg**  
> 🍽️ **Suggested preparation:** *~480–500 meals* based on historical consumption.

---

## 📁 Dataset Overview (`train.csv`)

| Column | Description |
|--------|-------------|
| `date` | Calendar date |
| `meals_served` | Meals eaten on the day |
| `temperature_C`, `humidity_percent` | Weather conditions |
| `day_of_week` | 0=Mon, 6=Sun |
| `special_event` | 1 if event day |
| `kitchen_staff`, `staff_experience` | Operational data |
| `past_waste_kg` | Previous day waste |
| `waste_category` | Food category wasted |
| `food_waste_kg` | **Daily food waste (Target variable)** |

### 🎯 Why `food_waste_kg` is the Target?

Although we could predict how many meals will be served, this dataset **is more strongly correlated with waste behavior than demand**.  
Predicting waste directly allows:

- More accurate forecasting  
- Direct CO₂ estimation  
- Immediate sustainability recommendations  

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
