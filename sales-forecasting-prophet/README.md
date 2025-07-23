# 📈 Sales Forecasting with Facebook Prophet

This project demonstrates time series forecasting on real-world retail sales data using the **Facebook Prophet** model.  
It includes data preparation, exploratory analysis, forecasting, and seasonality breakdown.

---

## 🧾 Dataset

- **Source**: [Sales Data Sample – Kaggle](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)
- **Rows**: 2,800+ order-level records
- **Period**: 2003–2005
- **Target**: Daily total sales (`SALES`), aggregated from individual transactions

---

## 🔧 Tools & Libraries

- Python, pandas, matplotlib, seaborn
- `prophet` (formerly fbprophet)

---

## 📊 Project Workflow

1. **Data Loading & Cleaning**
   - Converted `ORDERDATE` to datetime
   - Selected relevant fields: `ORDERDATE` and `SALES`

2. **Aggregation & EDA**
   - Grouped sales by day
   - Visualized sales trends over time

3. **Forecasting**
   - Trained Prophet on daily sales
   - Predicted next 90 days with confidence intervals

4. **Seasonality Analysis**
   - Detected weekly and yearly patterns
   - Monday and Saturday dips, holiday peaks in November–December

---

## 🔍 Key Insights

- Prophet captured noisy seasonal behavior and revealed strong yearly trends.
- Holidays show sales peaks, while weekends are typically slower.
- This type of forecast is valuable for stock planning, marketing campaigns, and logistics.

---

## 📁 Files

- `sales_forecasting_prophet.ipynb`: Full Colab notebook
- `sales_data_sample.csv`: Original dataset (or sample)
- `README.md`: This file

---

## ✅ Final Notes

This project demonstrates a clean and interpretable forecasting workflow using time series data.  
It can easily be extended with:
- **Holiday effects**
- **Extra regressors** (e.g. promotion, region, product line)
- **Train/test split + error metrics**
- Deployment via Streamlit or dashboard

---

## 🙋‍♀️ Author

**Eleni Dogranli**  
_Data Scientist | ML | Python | Forecasting_

📧 Contact: [LinkedIn](https://www.linkedin.com/in/eleni-dogranli) 
