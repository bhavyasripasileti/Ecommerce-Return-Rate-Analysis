import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression


st.set_page_config(page_title="Return Rate Dashboard", layout="wide")

# custom styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)


st.title("📊 E-Commerce Return Rate Dashboard")

# -----------------------
# Load Data
# -----------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_superstore.csv")

df = load_data()

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


# Create labels
df['Return_Label'] = df['Return'].map({0: "Not Returned", 1: "Returned"})

# Sample data
sample_df = df.sample(min(1500, len(df)), random_state=42)

# Split data manually (THIS AVOIDS WEBGL)
returned = sample_df[sample_df['Return_Label'] == "Returned"]
not_returned = sample_df[sample_df['Return_Label'] == "Not Returned"]

fig2 = go.Figure()

# Add traces 
fig2.add_trace(go.Scatter(
    x=not_returned['Discount'],
    y=not_returned['Profit'],
    mode='markers',
    name='Not Returned',
    opacity=0.5,
    marker=dict(color='cyan')
))

fig2.add_trace(go.Scatter(
    x=returned['Discount'],
    y=returned['Profit'],
    mode='markers',
    name='Returned',
    opacity=0.5,
    marker=dict(color='red')
))

fig2.update_layout(
    title="Discount vs Profit (Return Behavior)",
    template="plotly_dark",
    height=500,
    xaxis_title="Discount",
    yaxis_title="Profit"
)

st.plotly_chart(fig2, use_container_width=True)

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
