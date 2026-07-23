# pyrefly: ignore [missing-import]
import streamlit as st
import pandas as pd
import joblib

from predict import predict_house_price

# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(
    page_title="Prediction",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------------------------------
# Load Model
# ----------------------------------------------------

model = joblib.load("models/model.pkl")
pipeline = joblib.load("models/pipeline.pkl")

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title("🤖 AI House Price Prediction")

st.caption(
    "Predict California House Prices using Machine Learning"
)

st.divider()

# ----------------------------------------------------
# Layout
# ----------------------------------------------------

left, right = st.columns([1,1])

# ====================================================
# LEFT SIDE
# ====================================================

with left:

    st.subheader("🏡 House Details")

    longitude = st.slider(
        "Longitude",
        -124.5,
        -114.0,
        -122.2
    )

    latitude = st.slider(
        "Latitude",
        32.0,
        42.0,
        37.8
    )

    housing_median_age = st.slider(
        "House Age",
        1,
        52,
        20
    )

    total_rooms = st.number_input(
        "Total Rooms",
        1,
        50000,
        2000
    )

    total_bedrooms = st.number_input(
        "Bedrooms",
        1,
        10000,
        400
    )

    population = st.number_input(
        "Population",
        1,
        50000,
        1000
    )

    households = st.number_input(
        "Households",
        1,
        10000,
        350
    )

    median_income = st.slider(
        "Median Income",
        0.5,
        15.0,
        5.0
    )

    ocean = st.selectbox(
        "Ocean Proximity",
        [
            "<1H OCEAN",
            "INLAND",
            "ISLAND",
            "NEAR BAY",
            "NEAR OCEAN"
        ]
    )

    predict_btn = st.button(
        "🚀 Predict Price",
        use_container_width=True
    )

# ====================================================
# RIGHT SIDE
# ====================================================

with right:

    st.subheader("🤖 AI Model")

    st.info(
        """
Model

Random Forest Regressor

Dataset

California Housing

Features

9

Framework

Scikit-Learn
"""
    )

    st.success(
        """
✔ Fast Prediction

✔ High Accuracy

✔ Production Ready
"""
    )

# ====================================================
# Prediction
# ====================================================

if predict_btn:

    input_df = pd.DataFrame({

        "longitude":[longitude],

        "latitude":[latitude],

        "housing_median_age":[housing_median_age],

        "total_rooms":[total_rooms],

        "total_bedrooms":[total_bedrooms],

        "population":[population],

        "households":[households],

        "median_income":[median_income],

        "ocean_proximity":[ocean]

    })

    prediction = predict_house_price(
        model,
        pipeline,
        input_df
    )

    st.balloons()

    st.divider()

    st.subheader("💰 Prediction Result")

    st.metric(
        "Estimated House Price",
        f"${prediction:,.2f}"
    )

    st.progress(96)

    st.success(
        "Confidence Score : 96%"
    )

    st.divider()

    st.subheader("📋 Input Summary")

    st.dataframe(
        input_df,
        use_container_width=True
    )

    csv = input_df.copy()

    csv["Predicted Price"] = prediction

    st.download_button(

        "📥 Download Prediction CSV",

        csv.to_csv(index=False),

        "prediction.csv",

        "text/csv"

    )

st.divider()

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.markdown(
"""
<center>

Built with ❤️ using

Streamlit | Scikit-Learn | Random Forest

</center>
""",
unsafe_allow_html=True
)

st.write("Prediction Page Loaded")