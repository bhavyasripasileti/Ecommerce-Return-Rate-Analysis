import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression

# ------------------ CONFIG ------------------
st.set_page_config(page_title="E-commerce Return Rate Dashboard", layout="wide")

# ------------------ STYLE ------------------
st.markdown("""
<style>
.stApp { background-color: #0E1117; }
h1, h2, h3 { color: #EAEAEA; }
</style>
""", unsafe_allow_html=True)

# ------------------ LOAD DATA ------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_superstore.csv")
    df['Return'] = df['Profit'].apply(lambda x: 1 if x < 0 else 0)
    return df

df = load_data()

# ------------------ SIDEBAR ------------------
st.sidebar.header("🔎 Filters")

category = st.sidebar.multiselect(
    "Category", df['Category'].unique(),
    default=df['Category'].unique()
)

df = df[df['Category'].isin(category)]

# ------------------ HEADER ------------------
st.title("🛒 E-commerce Return Rate Dashboard")
st.caption("Analyze return patterns & predict high-risk orders")

# ------------------ KPI ------------------
st.markdown("## 📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Orders", len(df))
col2.metric("Return Rate", f"{df['Return'].mean()*100:.2f}%")
col3.metric("Total Sales", f"${df['Sales'].sum():,.0f}")

st.markdown("---")

# ------------------ CATEGORY RETURNS ------------------
st.markdown("## 📦 Returns by Category")

cat = df.groupby("Category")['Return'].mean().reset_index()

fig1 = px.bar(cat, x="Category", y="Return", color="Category", text_auto=True)
fig1.update_layout(template="plotly_dark")

st.plotly_chart(fig1, use_container_width=True)

st.info("📌 Furniture & Office Supplies show higher return rates.")

st.markdown("---")

# ------------------ DISCOUNT ANALYSIS ------------------
st.markdown("## 💸 Discount vs Return")

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

# ------------------ ML MODEL ------------------
features = ['Sales', 'Quantity', 'Discount']
X = df[features]
y = df['Return']

model = LogisticRegression()
model.fit(X, y)

df['Risk'] = model.predict_proba(X)[:, 1]

# ------------------ HIGH RISK ------------------
st.markdown("## ⚠️ High Risk Orders")

threshold = st.slider("Risk Threshold", 0.0, 1.0, 0.6)

high_risk = df[df['Risk'] > threshold]

st.dataframe(high_risk.head(20), use_container_width=True)

st.download_button(
    "📥 Download High Risk Orders",
    high_risk.to_csv(index=False),
    file_name="high_risk_orders.csv"
)

st.markdown("---")

# ------------------ PREDICTOR ------------------
st.markdown("## 🤖 Return Risk Predictor")

col1, col2, col3 = st.columns(3)

sales = col1.number_input("Sales", 0.0, 10000.0, 100.0)
quantity = col2.slider("Quantity", 1, 10, 2)
discount = col3.slider("Discount", 0.0, 1.0, 0.2)

if st.button("Predict"):
    pred = model.predict_proba([[sales, quantity, discount]])[0][1]

    if pred > 0.6:
        st.error(f"⚠️ High Return Risk: {pred:.2%}")
    else:
        st.success(f"✅ Low Return Risk: {pred:.2%}")
