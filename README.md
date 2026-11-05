# 🩺 Diabetes Risk Screening & Prediction Tool
> An AI-powered bilingual (Arabic/English) web application for early screening of diabetes risk based on health and lifestyle indicators.

---

## 📌 Project Overview
This project aims to build an interpretable machine learning model to estimate individual diabetes risk using the **CDC Behavioral Risk Factor Surveillance System (BRFSS)** dataset. Designed primarily as an educational screening tool, the application focuses on maximizing **Recall** to minimize false negatives in medical screening.

- **Deployed App**: *(ضع رابط تطبيق Streamlit Cloud هنا بعد النشر)*
- **Model Standard**: Scikit-Learn Pipelines with `RobustScaler` and `LogisticRegression`.

---

## 📊 Model Performance Comparison

Three machine learning models were trained and tuned using 5-fold `StratifiedKFold` Cross-Validation:

| Model | ROC-AUC Score | Primary Focus | Status |
| :--- | :---: | :---: | :---: |
| **Logistic Regression** | **0.7736** | High Recall / Linear Separability | **Selected Best Model** |
| **Random Forest** | 0.7335 | Non-linear ensemble | Baseline Comparison |
| **Decision Tree** | 0.5605 | Single Tree Baseline | Overfitted |

---

## 🔑 Key Risk Factors Identified
Based on model coefficient analysis, the top health indicators driving diabetes risk are:
1. **Heart Disease / Attack History** (`HeartDiseaseorAttack`)
2. **High Blood Cholesterol** (`HighChol`)
3. **Stroke History** (`Stroke`)
4. **High Blood Pressure** (`HighBP`)
5. **Smoking History** (`Smoker`)
6. **Difficulty Walking / Stairs** (`DiffWalk`)
7. **General Health Self-Rating** (`GenHlth`)

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/diabetes-risk-screening.git](https://github.com/your-username/diabetes-risk-screening.git)
   cd diabetes-risk-screening