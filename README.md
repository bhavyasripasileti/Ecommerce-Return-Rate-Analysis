# E-Commerce Return Rate Reduction Analysis

## 📌 Project Overview
This project focuses on analyzing e-commerce sales data to understand return patterns and identify high-risk products that are more likely to be returned. Using data analysis, basic machine learning, and an interactive Tableau dashboard, the project provides actionable insights to help reduce return rates and improve business decision-making.

This project was completed as part of an **Industry Internship at Elevate Labs**.

---

## 🎯 Objectives
- Analyze historical e-commerce order data to identify return trends
- Understand the impact of discounts on return behavior
- Identify categories and sub-categories with high return rates
- Predict high-risk orders using a machine learning model
- Visualize insights using an interactive Tableau dashboard

---

## 📊 Dataset Description
- **Source:** Superstore-style E-commerce Dataset
- **Format:** CSV
- **Records:** ~10,000 orders
- **Key Features:**
  - Order ID, Order Date, Ship Mode
  - Category, Sub-Category, Product Name
  - Sales, Quantity, Discount, Profit

A return flag was logically derived:
- Orders with **negative profit** were treated as returned/problematic orders.

---

## 🛠️ Tools & Technologies Used
- **Python (Google Colab)**
  - Pandas, NumPy
  - Scikit-learn
- **Machine Learning**
  - Logistic Regression (Return Risk Prediction)
- **Visualization**
  - Tableau Public
- **Version Control**
  - GitHub

---

## 🔄 Project Workflow
1. **Data Loading & Cleaning**
   - Handled encoding issues
   - Removed missing values
   - Created a return indicator using profit values

2. **Exploratory Data Analysis (EDA)**
   - Return rate analysis by category and sub-category
   - Discount vs return behavior analysis

3. **Machine Learning Model**
   - Built a Logistic Regression model
   - Predicted return probability for each order
   - Identified high-risk orders (Return Probability > 60%)

4. **Dashboard Creation**
   - Designed an interactive Tableau dashboard
   - Visualized KPIs, trends, and high-risk product groups

---

## 📈 Key Insights
- Overall return rate is approximately **18–19%**
- **Furniture and Office Supplies** show higher return rates
- Higher discount levels significantly increase return probability
- Certain sub-categories consistently exhibit high return risk
- High-risk products were identified with return probability above 60%

---

## 📊 Tableau Dashboard
An interactive dashboard was created using Tableau Public to visualize the insights.

📌 **Dashboard Link:**  
`https://public.tableau.com/app/profile/bhavya.sri.pasileti/viz/EcommerceReturnRateAnalysis/E-CommerceReturnRateReductionAnalysis?publish=yes`

---

## 📁 Repository Structure

Ecommerce-Return-Rate-Analysis

│

├── data/

│ ├── superstore.csv

│ ├── cleaned_superstore.csv

│ └── high_risk_orders.csv

│

├── notebook/

│ ├── ecommerce_return_rate_analysis.ipynb

│

├── dashboard/

│ └── tableau_dashboard_link.txt

│

└── README.md


---

## ✅ Conclusion
This project demonstrates an end-to-end data analytics workflow, from raw data processing to actionable insights and dashboard deployment. The results can help businesses proactively identify risky products, optimize discount strategies, and reduce return-related losses.

---

## 👤 Author
**Bhavya Sri Pasileti**   
Data Analyst Intern – Elevate Labs  
