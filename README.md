<div align="center">

# 📦 E-Commerce Return Rate Reduction Analysis

### Identify high-risk orders, reduce returns, and optimize business decisions using data & AI.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://streamlit.io)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)](https://scikit-learn.org)
[![Tableau](https://img.shields.io/badge/Tableau-Visualization-E97627?style=for-the-badge\&logo=tableau\&logoColor=white)](https://tableau.com)
[![Pandas](https://img.shields.io/badge/Pandas-Data--Analysis-150458?style=for-the-badge\&logo=pandas\&logoColor=white)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

<br/>

> An end-to-end **data analytics & machine learning project** that analyzes e-commerce return behavior, identifies high-risk products, and provides actionable insights through interactive dashboards.

<br/>

**[📊 Workflow](#-project-workflow) · [📦 Setup](#-getting-started) · [✨ Features](#-key-features)**

</div>

---

## 🌐 Live App

> 🔗 **[Click here to explore the dashboard »](https://ecommerce-return-rate-analysis-j3n535u5nsh6nczbuhvkwk.streamlit.app/)**


---

## 🌐 Overview

E-commerce businesses often face significant losses due to high return rates.

This project analyzes order data to **identify return patterns, understand influencing factors (like discounts), and predict high-risk orders** using machine learning.

It combines **EDA + ML + Dashboarding (Streamlit & Tableau)** to deliver a complete decision-support system.

---

## ✨ Key Features

| Feature                     | Description                                        |
| --------------------------- | -------------------------------------------------- |
| 📊 Data Analysis            | Explore return trends across categories & products |
| 🩺 Return Pattern Detection | Identify high-return segments                      |
| 🤖 ML Prediction            | Logistic Regression model to predict return risk   |
| 📉 Discount Impact Analysis | Understand how discounts affect returns            |
| 📦 High-Risk Identification | Flag orders with >60% return probability           |
| 🖥️ Interactive Dashboards  | Streamlit + Tableau visualizations                 |

---

## 📊 Dataset Description

* **Source:** Superstore-style E-commerce dataset
* **Records:** ~10,000 orders
* **Format:** CSV

### Key Features:

* Order ID, Order Date, Ship Mode
* Category, Sub-Category, Product Name
* Sales, Quantity, Discount, Profit

### 📌 Return Logic:

* Orders with **negative profit → classified as returned/problematic**

---

## ⚙️ Project Workflow

```
Data Collection → Data Cleaning → EDA → Feature Engineering
        │
        ▼
Machine Learning (Logistic Regression)
        │
        ▼
Return Risk Prediction
        │
        ▼
Visualization (Streamlit + Tableau Dashboards)
```

### 🔄 Detailed Steps

1. **Data Cleaning**

   * Handled missing values and inconsistencies
   * Created return indicator

2. **Exploratory Data Analysis**

   * Category-wise return trends
   * Discount vs return behavior

3. **Model Building**

   * Logistic Regression classifier
   * Predicted return probability

4. **Risk Classification**

   * High-risk orders: Probability > 60%

5. **Dashboard Development**

   * Streamlit dashboard (interactive analytics)
   * Tableau dashboard (business insights)

---

## 📈 Key Insights

* 📌 Overall return rate: **~18–19%**
* 🪑 Furniture & Office Supplies have higher return rates
* 💸 Higher discounts → higher return probability
* 📦 Certain sub-categories consistently show high return risk
* ⚠️ High-risk orders identified using ML model

---

## 🖥️ Dashboard

### 📊 Tableau Dashboard

🔗 https://public.tableau.com/app/profile/bhavya.sri.pasileti/viz/EcommerceReturnRateAnalysis/E-CommerceReturnRateReductionAnalysis?publish=yes

### 🚀 Streamlit Dashboard

> Interactive app for real-time analysis and prediction

Run locally:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
Ecommerce-Return-Rate-Analysis/
│
├── data/
│   ├── superstore.csv
│   ├── cleaned_superstore.csv
│   └── high_risk_orders.csv
│
├── notebook/
│   └── ecommerce_return_rate_analysis.ipynb
│
├── dashboard/
│   ├── app.py                # Streamlit dashboard
│   └── tableau_dashboard_link.txt
│
├── model/
│   └── return_model.pkl      # Trained ML model
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Category         | Technology                         |
| ---------------- | ---------------------------------- |
| Language         | Python                             |
| Data Processing  | Pandas, NumPy                      |
| Machine Learning | Scikit-learn (Logistic Regression) |
| Visualization    | Streamlit, Tableau                 |
| Notebook         | Google Colab                       |
| Version Control  | GitHub                             |

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Ecommerce-Return-Rate-Analysis.git
cd Ecommerce-Return-Rate-Analysis
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run dashboard/app.py
```

---

## 🔮 Future Improvements

* Advanced models (Random Forest, XGBoost)
* Real-time return prediction API
* Integration with e-commerce platforms
* Customer behavior analysis
* Automated retraining pipeline

---

## 💼 Project Highlights

* Built a complete **end-to-end data analytics pipeline**
* Combined **EDA + ML + dashboarding**
* Developed **real-world business use case solution**
* Implemented **risk prediction using Logistic Regression**
* Delivered insights via **interactive dashboards**

---

## 📜 License

MIT License — free to use and modify.

---

## 👤 Author

**Bhavya Sri Pasileti**

> Data Science & AI Enthusiast
> Passionate about solving real-world problems using data.

---

<div align="center">

⭐ If you found this project useful, give it a star!

*Built with ❤️ by Bhavya Sri Pasileti*

</div>
