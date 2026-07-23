# pyrefly: ignore [missing-import]
import streamlit as st
import pandas as pd
# pyrefly: ignore [missing-import]
import plotly.express as px
# pyrefly: ignore [missing-import]
import plotly.graph_objects as go

# --------------------------------------
# Page Config
# --------------------------------------

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------
# Load Dataset
# --------------------------------------

df = pd.read_csv("data/housing.csv")

# --------------------------------------
# Title
# --------------------------------------

st.title("📊 California Housing Analytics")

st.caption(
    "Interactive Dashboard for Dataset Exploration"
)

st.divider()

# ======================================
# KPI Cards
# ======================================

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "🏠 Houses",
    len(df)
)

c2.metric(
    "📌 Features",
    df.shape[1]-1
)

c3.metric(
    "💰 Avg Price",
    f"${df['median_house_value'].mean():,.0f}"
)

c4.metric(
    "💵 Avg Income",
    round(df["median_income"].mean(),2)
)

st.divider()

# ======================================
# Dataset Preview
# ======================================

st.subheader("📂 Dataset Preview")

st.dataframe(
    df.head(),
    use_container_width=True
)

st.divider()

# ======================================
# Price Distribution
# ======================================

st.subheader("💰 House Price Distribution")

fig = px.histogram(
    df,
    x="median_house_value",
    nbins=50,
    title="Distribution of House Prices"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ======================================
# Income vs Price
# ======================================

st.subheader("📈 Income vs House Price")

fig = px.scatter(

    df.sample(3000),

    x="median_income",

    y="median_house_value",

    color="housing_median_age",

    size="population",

    title="Median Income vs House Price"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ======================================
# Ocean Distribution
# ======================================

st.subheader("🌊 Ocean Proximity")

ocean = df["ocean_proximity"].value_counts().reset_index()

ocean.columns = ["Ocean","Count"]

fig = px.pie(

    ocean,

    values="Count",

    names="Ocean",

    hole=0.45

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ======================================
# California Map
# ======================================

st.subheader("🌍 California Housing Map")

map_df = df.rename(
    columns={
        "latitude":"lat",
        "longitude":"lon"
    }
)

fig = px.scatter_map(
    map_df.sample(3000),
    lat="lat",
    lon="lon",
    color="median_house_value",
    zoom=4,
    height=650,
    map_style="carto-positron"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ======================================
# Correlation Heatmap
# ======================================

st.subheader("🔥 Correlation Matrix")

corr = df.select_dtypes(include="number").corr()

fig = go.Figure(
    data=go.Heatmap(

        z=corr.values,

        x=corr.columns,

        y=corr.columns,

        colorscale="Viridis",

        text=corr.round(2),

        texttemplate="%{text}"

    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ======================================
# Statistics
# ======================================

st.subheader("📋 Dataset Statistics")

st.dataframe(

    df.describe(),

    use_container_width=True

)

st.divider()

# ======================================
# Footer
# ======================================

st.markdown(
"""
<center>

Built with ❤️ using Streamlit & Plotly

</center>
""",
unsafe_allow_html=True
)