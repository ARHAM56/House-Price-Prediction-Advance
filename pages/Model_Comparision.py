# pyrefly: ignore [missing-import]
import streamlit as st
import pandas as pd
import numpy as np
# pyrefly: ignore [missing-import]
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

st.set_page_config(
    page_title="Model Comparison",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Machine Learning Model Comparison")

# -----------------------------
# Load Dataset
# -----------------------------

try:
    df = pd.read_csv("data/housing.csv")
except Exception as e:
    st.error(f"Dataset not found.\n\n{e}")
    st.stop()

# -----------------------------
# Prepare Data
# -----------------------------

X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

numeric_cols = X.drop("ocean_proximity", axis=1).columns.tolist()
categorical_cols = ["ocean_proximity"]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

pipeline = ColumnTransformer([
    ("num", numeric_pipeline, numeric_cols),
    ("cat", categorical_pipeline, categorical_cols)
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

X_train = pipeline.fit_transform(X_train)
X_test = pipeline.transform(X_test)

# -----------------------------
# Models
# -----------------------------

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
}

results = []

with st.spinner("Training models..."):

    for name, model in models.items():

        model.fit(X_train, y_train)

        pred = model.predict(X_test)

        mae = mean_absolute_error(y_test, pred)

        rmse = np.sqrt(mean_squared_error(y_test, pred))

        r2 = r2_score(y_test, pred)

        results.append({
            "Model": name,
            "MAE": round(mae, 2),
            "RMSE": round(rmse, 2),
            "R² Score": round(r2, 4)
        })

results = pd.DataFrame(results)

st.success("✅ Training Complete")

st.subheader("Performance Table")

st.dataframe(results, use_container_width=True)

# -----------------------------
# Best Model
# -----------------------------

best = results.loc[results["RMSE"].idxmin()]

st.success(f"""
🏆 Best Model

**{best['Model']}**

RMSE : **{best['RMSE']}**

R² Score : **{best['R² Score']}**
""")

# -----------------------------
# RMSE
# -----------------------------

fig = px.bar(
    results,
    x="Model",
    y="RMSE",
    color="Model",
    text="RMSE",
    title="RMSE Comparison"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# MAE
# -----------------------------

fig = px.bar(
    results,
    x="Model",
    y="MAE",
    color="Model",
    text="MAE",
    title="MAE Comparison"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# R2
# -----------------------------

fig = px.bar(
    results,
    x="Model",
    y="R² Score",
    color="Model",
    text="R² Score",
    title="R² Score Comparison"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Conclusion
# -----------------------------

st.info("""
### 📌 Model Summary

- Linear Regression is the simplest model.
- Decision Tree captures nonlinear relationships but may overfit.
- Random Forest generally provides the best performance for this dataset.

Random Forest is recommended for production use.
""")