# Walmart Sales Forecasting App

An interactive Streamlit web app that predicts weekly sales for Walmart stores and departments using a tuned XGBoost model. Built as a portfolio project to showcase skills in data science, forecasting, and app deployment.

##  Features

-  Filter sales forecasts by **store**, **department**, and **date range**
-  Interactive **line chart** for predicted weekly sales
-  Real-time **summary metrics**: total & average sales
-  **Heatmap** of forecasted sales by department and store
-  **Download filtered forecast** as CSV
-  **Live on Streamlit Cloud** for public access

## Model Performance

- **Algorithm**: XGBoost Regressor
- **R² Score**: `0.8612` — explains ~86% of sales variance
- **RMSE**: ~$8,509
- **MAE**: ~$4,832  
Trained on over **45,000 weekly records** across multiple Walmart locations.

## Dataset

- Source: [Kaggle – Walmart Sales Forecasting](https://www.kaggle.com/datasets/aslanahmedov/walmart-sales-forecast)
- Includes weekly sales, markdown events, holidays, and economic indicators

## Live App

[Launch the Streamlit App]([👉 Launch the Streamlit App](https://walmart-sales.streamlit.app/)

## Tech Stack

- **Python**, **Pandas**, **XGBoost**
- **Matplotlib**, **Seaborn**
- **Streamlit** for UI & deployment
- **Git** & **GitHub** for version control

## Project Structure
├── app.py # Streamlit application
├── walmart_forecast_output.csv # Forecast results for test set
├── train.csv, test.csv # Kaggle dataset
├── stores.csv, features.csv # Additional data
├── charts/ # Optional: visualizations
└── README.md


## ✍️ Author

**Giulio Piccinonna**  
Graduate Student – M.S. Data Analytics, UCF  
[GitHub](https://github.com/jules-ml) • [Portfolio](https://julesdata.carrd.co) *(replace this)*

---


