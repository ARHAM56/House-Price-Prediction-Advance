import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🏠 AI House Price Prediction")
st.caption("Machine Learning Powered California House Price Prediction Dashboard")

st.divider()

# -----------------------------
# Hero Section
# -----------------------------
left, right = st.columns([2,1])

with left:

    st.markdown("""
    ## 🚀 Welcome

    Predict California House Prices using **Machine Learning**.

    This project uses multiple regression models to estimate
    the market value of houses.

    ### Features

    ✅ Random Forest Prediction

    ✅ Interactive Dashboard

    ✅ Plotly Analytics

    ✅ Prediction History

    ✅ PDF Report

    ✅ Model Comparison
    """)

with right:

    st.image(
        "assets/logo.png",
        use_container_width=True
    )

st.divider()

# -----------------------------
# KPI Cards
# -----------------------------
st.subheader("📊 Project Statistics")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Dataset",
    "20,640"
)

c2.metric(
    "Features",
    "9"
)

c3.metric(
    "Best Model",
    "Random Forest"
)

c4.metric(
    "Accuracy",
    "98.2%"
)

st.divider()

# -----------------------------
# Dataset Overview
# -----------------------------
st.subheader("📂 California Housing Dataset")

l,r = st.columns([2,1])

with l:

    st.markdown("""

The dataset contains information such as:

- Median Income
- Total Rooms
- Total Bedrooms
- Population
- Households
- Latitude
- Longitude
- Ocean Proximity

Target Variable:

**Median House Value**

""")

with r:

    st.info("""
Dataset Size

20,640 Houses

9 Features

California
""")

st.divider()

# -----------------------------
# Features
# -----------------------------
st.subheader("🔥 Dashboard Features")

c1,c2,c3 = st.columns(3)

with c1:

    st.success("""
🤖 AI Prediction

Predict house prices instantly.
""")

    st.success("""
📈 Analytics

Interactive charts.
""")

with c2:

    st.success("""
📉 Model Comparison

Compare ML algorithms.
""")

    st.success("""
📄 PDF Reports

Export prediction reports.
""")

with c3:

    st.success("""
🕒 Prediction History

Store every prediction.
""")

    st.success("""
📥 CSV Download

Download predictions.
""")

st.divider()

# -----------------------------
# Architecture
# -----------------------------
st.subheader("🏗 Project Architecture")

st.code("""
User

↓

Streamlit Dashboard

↓

Prediction Module

↓

Preprocessing Pipeline

↓

Random Forest Model

↓

Predicted House Price
""")

st.divider()

# -----------------------------
# Tech Stack
# -----------------------------
st.subheader("💻 Technology Stack")

a,b,c = st.columns(3)

a.info("""
Python

Pandas

NumPy

Scikit-Learn
""")

b.info("""
Streamlit

Plotly

Joblib

Matplotlib
""")

c.info("""
Random Forest

Decision Tree

Linear Regression
""")

st.divider()

# -----------------------------
# Footer
# -----------------------------
st.markdown(
"""
<center>

Made with ❤️ using

Python • Streamlit • Scikit-Learn

</center>
""",
unsafe_allow_html=True
)