# pyrefly: ignore [missing-import]
import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("ℹ️ About This Project")
st.markdown("---")

st.write("""
Welcome to the **AI House Price Prediction Dashboard**.

This application uses Machine Learning to predict California house prices
based on different housing features.

The project demonstrates a complete Machine Learning workflow from
data preprocessing to deployment using Streamlit.
""")

# -----------------------------
# Project Overview
# -----------------------------
st.header("🏠 Project Overview")

col1, col2 = st.columns(2)

with col1:
    st.info("""
### Objective

Predict house prices using Machine Learning.

The application includes:

- Data Analysis
- House Price Prediction
- Model Comparison
- Interactive Dashboard
- Modern User Interface
""")

with col2:
    st.success("""
### Dataset

California Housing Dataset

- 20,640 Records
- 9 Features
- Regression Problem
- Numerical + Categorical Data
""")

st.markdown("---")

# -----------------------------
# Technology Stack
# -----------------------------
st.header("💻 Technology Stack")

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("Programming")

    st.write("""
- Python
- Pandas
- NumPy
""")

with c2:
    st.subheader("Machine Learning")

    st.write("""
- Scikit-Learn
- Random Forest
- Decision Tree
- Linear Regression
""")

with c3:
    st.subheader("Visualization")

    st.write("""
- Streamlit
- Plotly
- Matplotlib
""")

st.markdown("---")

# -----------------------------
# Project Features
# -----------------------------
st.header("🚀 Features")

st.write("""
✅ House Price Prediction

✅ Data Analytics Dashboard

✅ Interactive Charts

✅ Model Comparison

✅ CSV Download

✅ Responsive Streamlit UI

✅ Machine Learning Pipeline

✅ Professional Dashboard
""")

st.markdown("---")

# -----------------------------
# ML Workflow
# -----------------------------
st.header("🤖 Machine Learning Workflow")

st.code("""
Housing Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Missing Value Handling
        │
        ▼
Feature Scaling
        │
        ▼
One Hot Encoding
        │
        ▼
Train/Test Split
        │
        ▼
Random Forest Training
        │
        ▼
Prediction
        │
        ▼
Streamlit Dashboard
""")

st.markdown("---")

# -----------------------------
# Folder Structure
# -----------------------------
st.header("📁 Folder Structure")

st.code("""
House-Price-Prediction/

│
├── app.py
├── train.py
├── predict.py
├── requirements.txt
│
├── pages/
│   ├── 1_Home.py
│   ├── 2_Prediction.py
│   ├── 3_Analytics.py
│   ├── 4_Model_Comparison.py
│   └── 5_About.py
│
├── assets/
├── data/
├── models/
└── reports/
""")

st.markdown("---")

# -----------------------------
# Future Scope
# -----------------------------
st.header("🌟 Future Enhancements")

st.write("""
- User Authentication
- PDF Report Generation
- SHAP Explainability
- XGBoost Model
- Deep Learning Model
- Cloud Deployment
- Docker Support
- REST API
""")

st.markdown("---")

# -----------------------------
# Developer
# -----------------------------
st.header("👨‍💻 Developer")

st.info("""
**Arham Aziz**

B.Tech Artificial Intelligence & Machine Learning

Skills:

• Python

• Java

• Spring Boot

• Machine Learning

• SQL

• Streamlit

• Data Analytics
""")

st.markdown("---")

st.success("Thank you for exploring this project! 🚀")

st.caption("Built using Python • Streamlit • Scikit-Learn • Plotly")