import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="Return Rate Dashboard", layout="wide")

# custom styling
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 E-Commerce Return Rate Dashboard")

# -----------------------
# Load Data
# -----------------------
df = pd.read_csv("data/cleaned_superstore.csv")

# Create Return Column
df['Return'] = df['Profit'].apply(lambda x: 1 if x < 0 else 0)

# -----------------------
# KPIs
# -----------------------
total_orders = len(df)
return_rate = df['Return'].mean() * 100

col1, col2 = st.columns(2)
col1.metric("Total Orders", total_orders)
col2.metric("Return Rate (%)", f"{return_rate:.2f}")

# -----------------------
# Category Analysis
# -----------------------
st.subheader("📦 Returns by Category")

cat = df.groupby("Category")['Return'].mean().reset_index()

fig = px.bar(cat, x="Category", y="Return", color="Category")
st.plotly_chart(fig)

# -----------------------
# Discount Analysis
# -----------------------
st.subheader("💸 Discount vs Profit")

fig2 = px.scatter(df, x="Discount", y="Profit", color="Return")
st.plotly_chart(fig2)

# -----------------------
# ML Prediction
# -----------------------
st.subheader("🤖 Predict Return")

features = ['Sales', 'Quantity', 'Discount']
X = df[features]
y = df['Return']

model = LogisticRegression()
model.fit(X, y)

sales = st.number_input("Sales", 0.0, 10000.0, 100.0)
quantity = st.slider("Quantity", 1, 10, 2)
discount = st.slider("Discount", 0.0, 1.0, 0.2)

if st.button("Predict"):
    pred = model.predict_proba([[sales, quantity, discount]])[0][1]
    st.success(f"Return Probability: {pred:.2%}")
