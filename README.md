# 🌱 **EcoServe-AI**  
### Smart Food Waste Forecasting & Sustainability Assistant

EcoServe-AI is a machine learning system that helps cafeterias **prevent food waste before it happens.**  
Instead of reacting after food is thrown away, EcoServe-AI **predicts tomorrow’s waste**, estimates its **CO₂ impact**, and **recommends a safe reduction in meal preparation** to avoid overproduction **without risking shortages.**

🚀 **Live Demo:**  
👉 https://your-streamlit-app-url.streamlit.app/

---

## 🚩 **Designed For**
Institutional kitchens that prepare 300+ meals/day:
- 🏫 Universities  
- 🏥 Hospitals  
- 🏢 Corporate cafeterias  

---

## ❗ Why Food Waste Happens

Kitchen managers prepare extra food because tomorrow’s attendance is unpredictable.  
To avoid complaints or shortages, they **overcook “just in case.”**  
However, this habit creates:

| Impact | Description |
|--------|-------------|
| 🍱 Food Waste | Leftover meals are discarded daily |
| 💸 Financial Loss | Ingredients, labor, gas/electricity, water wasted |
| 🌍 CO₂ Emissions | Decomposing food releases greenhouse gases |

### 📌 Real-World Example (University Cafeteria)

| Metric | Typical Value |
|--------|---------------|
| Daily meals cooked | 500–600 |
| Food leftover | 15–20% |


---

## 🎯 **What EcoServe-AI Solves**

Kitchen staff already *know* overproduction causes waste.  
EcoServe-AI answers a question they **can’t calculate manually**:

> ✔️ **How much can we safely reduce tomorrow’s meals without running short?**

By analyzing cooking behavior, past waste, events, weather, and temporal patterns, EcoServe-AI **provides a precise, data-backed reduction in planned meals.**

---

## 📊 💡 System Outputs

### EcoServe-AI Produces:
- **Predicted food waste (kg)**
- **Estimated CO₂ emissions**
- **Recommended number of meals to cook safely**
- **Waste % vs. sustainability threshold**

### 🌍 Default Sustainability Rules

| Parameter | Value |
|-----------|-------|
| Avg. meal weight | 0.8 kg |
| Emission factor | 2.5 kg CO₂ per 1 kg waste |
| Waste tolerance | 10% of meals cooked |

---

## 🧠 Example Recommendation

```
📍 Planned meals for tomorrow: 500

Predicted waste: 57.8 kg  
Estimated CO₂: 144.5 kg  
Waste ratio: 14.5%
```

### 🛠 Recommendation
> ♻️ **Reduce tomorrow’s preparation from 500 → 450 meals.**  
> This keeps waste under a 10% sustainability target and avoids food shortage.

---

## 🔗 Live Deployment (API)

**Hosted on Render**  
👉 Use `https://ecoserve-ai.onrender.com/docs` for interactive Swagger UI.

### 🟢 POST `/predict`

#### 📤 Request Example:
```json
{
  "meals_served": 500,
  "kitchen_staff": 12,
  "temperature_C": 29.5,
  "humidity_percent": 57.0,
  "day_of_week": 3,
  "special_event": 0,
  "past_waste_kg": 40.0,
  "staff_experience": "intermediate",
  "waste_category": "mixed",
  "month": 11,
  "is_weekend": 0,
  "planned_meals": 500
}
```

#### 📥 Response Example:
```json
{
  "predicted_waste_kg": 57.8,
  "estimated_co2_emission": 144.51,
  "waste_percent": 14.5,
  "suggested_meals": 450,
  "message": "Predicted waste is high. Consider reducing meals from 500 to 450."
}
```

---

## 📂 Project Structure

```
EcoServe-AI/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Data_Preprocessing_and_Model_Training.ipynb
├── src/
│   ├── train_model.py
│   ├── inference.py
│   └── recommendation.py
├── api/
│   └── main.py
├── models/
│   └── ecoserve_model.pkl
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🌟 Impact Summary

| Benefit | Result |
|---------|-------|
| ♻️ Reduced food waste | 10–20% saved monthly |
| 🌍 Lower CO₂ emissions | Direct reduction in greenhouse gases |
| 💸 Operational savings | Fewer ingredient, labor, gas, electricity losses |
| 📈 Smarter planning | Precision instead of guessing |
| 🙅 No shortage risk | Safety-margin-based recommendations |

> **EcoServe-AI turns intuition into precise, measurable, and sustainable action.**

---
