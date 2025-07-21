# 📉 Customer Churn Prediction

This project uses real-world data from a telecom company to predict which customers are most likely to leave ("churn") using machine learning techniques.

## 📊 Dataset
- Source: [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- 7,032 cleaned customer records
- Features include contract type, charges, services used, tenure, and payment method.

## ⚙️ Workflow

1. **Data Cleaning**: Handled missing values in `TotalCharges`, removed customer IDs.
2. **EDA**: Visualized relationships between churn and contract type, tenure, monthly charges.
3. **Encoding**: Applied one-hot encoding to categorical features.
4. **Modeling**: Trained two models:
   - Logistic Regression
   - Random Forest Classifier
5. **Evaluation**:
   - Logistic Regression accuracy: ~80%
   - Random Forest accuracy: ~79%
   - Precision/Recall tradeoffs analyzed
6. **Feature Importance**:
   - Key drivers of churn: `TotalCharges`, `tenure`, `MonthlyCharges`, `Contract Type`, `OnlineSecurity`

## 🔍 Key Insights

- Customers with **month-to-month contracts** are more likely to churn.
- Those with **short tenure** or **high monthly charges** are at higher risk.
- **Fiber optic users** and those paying with **electronic check** churn more.
- **Security & tech support services** appear to reduce churn.

## ✅ Business Recommendations

- Offer loyalty rewards or discounts to customers with short tenure and high monthly charges.
- Promote long-term contracts (1-2 years).
- Encourage use of online security and tech support tools.

## 📁 Files

- `churn_prediction_telco.ipynb`: Full project notebook
- `README.md`: This file

