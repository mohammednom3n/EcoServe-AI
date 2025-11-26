# 🌱 EcoServe-AI  
### Smart Food Waste Forecasting & Sustainability Assistant

**EcoServe-AI** is a machine learning system that helps institutional cafeterias reduce food waste **before it happens**.  
It predicts tomorrow’s food waste (kg), converts it to CO₂ emissions, and recommends how much to reduce meal preparation to stay within a sustainability threshold.

🚩 **Designed for:**  
- Universities  
- Hospitals  
- Corporate cafeterias  

…serving **more than 300 meals per day**.

---

## 📌 Problem Statement

Cafeterias frequently **over-prepare food** because tomorrow’s consumption is uncertain. Meal demand fluctuates due to:

- 🌡️ Weather conditions  
- 📅 Day of the week  
- 🎉 Events or celebrations  
- 👨‍🍳 Kitchen staff experience  
- ♻️ Leftovers or waste from the previous day  
- 🍽️ Seasonal or cultural meal patterns  

This leads to:

- 🍱 **Large quantities of edible food wasted**
- 💸 **Increased food purchasing and processing expenses**
- 🌍 **Higher CO₂ emissions from decomposing food**

> 📌 *Example (Typical University Cafeteria)*

| Metric | Value |
|--------|-------|
| Daily meal preparation | 500–600 meals |
| Food leftover | 15–25% |
| Monthly waste | 60–80 kg |
| Monthly CO₂ footprint | ~150–200 kg |

---

## 🎯 Project Objective

EcoServe-AI enables cafeterias to:

✔ **Forecast food waste before it occurs**  
✔ **Estimate the CO₂ footprint associated with wasted food**  
✔ **Receive actionable recommendations to reduce preparation safely**

💡 **EcoServe-AI provides a general forecasting framework that can be trained or fine-tuned using any cafeteria’s historical data, enabling adaptation to unique local consumption and cooking habits.**

📌 The system predicts **waste directly**, rather than predicting attendance first, providing more immediate and actionable sustainability insights.

---

## 🔬 System Workflow

### 📥 Inputs (provided by manager or system)
- 🍽️ `meals_served` (planned meals for tomorrow)
- 🌡️ `temperature_C`, `humidity_percent`
- 🎉 `special_event`
- 👨‍🍳 `kitchen_staff`, `staff_experience`
- ♻️ `past_waste_kg` (yesterday’s waste)
- 📅 `day_of_week`, `month`, `is_weekend`
- 🍗 `waste_category`

### 🤖 ML Model Output
- **Predicted food waste (kg)**

### 📊 Sustainability Calculations (Rule-Based)

| Metric | Formula |
|--------|---------|
| CO₂ emissions | `predicted_waste_kg × emission_factor` |
| Waste % of cooked food | `predicted_waste_kg / (meals_served × avg_meal_weight)` |
| Meal adjustment | If `waste% > threshold` → reduce meals |

#### Default Configurable Values

| Parameter | Default |
|-----------|---------|
| Avg. meal weight | 0.8 kg |
| Emission factor | 2.5 CO₂ kg per 1 kg waste |
| Waste tolerance | 10% |

---

## 🧾 Example Output

**Input (planned meals): 450**  
**Predicted waste:** 57.6 kg  
**Estimated CO₂:** ~144.0 kg  
**Waste ratio:** 16.0%

🔧 **Recommendation:**  
> Reduce preparation from **450 → 405 meals** to remain under a 10% waste tolerance.

---

## 📁 Dataset Overview (`train.csv`)

| Column | Description |
|--------|-------------|
| `date` | Calendar date |
| `meals_served` | Actual meals consumed on that day |
| `temperature_C`, `humidity_percent` | Weather inputs |
| `day_of_week`, `month`, `is_weekend` | Temporal context |
| `special_event` | Celebration or event indicator |
| `kitchen_staff`, `staff_experience` | Operational context |
| `past_waste_kg` | **Food waste from the previous day** |
| `waste_category` | Type of food commonly wasted |
| `food_waste_kg` | **Target: daily food waste (kg)** |

📌 **Why predict `food_waste_kg` directly?**  
Some cafeterias lack reliable attendance data due to exams, menu preferences, holidays, and salary cycles. Waste behavior, however, strongly reflects operational habits (overcooking, portion decisions, staff skill, leftovers).  
➡ **Predicting waste directly yields more practical and actionable sustainability decisions.**

> 📝 *Insert Heatmap Here:*  
> Place feature correlation heatmap below this section.  
> (Generated in `notebooks/01_EDA.ipynb`.)
  
---

## 🏗️ Project Structure

```bash
EcoServe-AI/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_Model_Training.ipynb
│   └── 04_Evaluation.ipynb
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── inference.py
│   └── recommendation.py
├── models/
│   └── ecoserve_food_waste_model.pkl
├── api/
│   └── main.py
├── README.md
└── requirements.txt
