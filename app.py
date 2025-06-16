import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load processed test set with predictions
test = pd.read_csv("walmart_forecast_output.csv")
test['Date'] = pd.to_datetime(test['Date'])

# App title
st.title("Walmart Weekly Sales Forecast")
st.markdown("""
Select a store and department to view forecasted weekly sales.
You can also explore overall trends and download the forecast data.
""")

# Sidebar filters
store_ids = sorted(test['Store'].unique())
dept_ids = sorted(test['Dept'].unique())

default_store = store_ids[0]
default_dept = dept_ids[0]

store = st.sidebar.selectbox("Select Store:", store_ids, index=store_ids.index(default_store))
dept = st.sidebar.selectbox("Select Department:", dept_ids, index=dept_ids.index(default_dept))

# Filtered DataFrame
filtered = test[(test['Store'] == store) & (test['Dept'] == dept)].copy()

# Date range filter — get min/max as pandas Timestamps
min_date, max_date = filtered['Date'].min(), filtered['Date'].max()

# Convert to native Python datetime.date for Streamlit slider
min_date = min_date.date()
max_date = max_date.date()

# Use date range slider
date_range = st.sidebar.slider(
    "Select Date Range:", 
    min_value=min_date, 
    max_value=max_date, 
    value=(min_date, max_date)
)

# Filter back to Pandas Timestamps
filtered = filtered[
    (filtered['Date'] >= pd.to_datetime(date_range[0])) & 
    (filtered['Date'] <= pd.to_datetime(date_range[1]))
]


# Display forecast plot
st.subheader(f"Forecasted Sales for Store {store}, Department {dept}")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(filtered['Date'], filtered['Weekly_Sales_Pred'], marker='o')
ax.set_title(f"Weekly Sales Forecast - Store {store} Dept {dept}")
ax.set_xlabel("Date")
ax.set_ylabel("Predicted Weekly Sales")
ax.grid(True)
st.pyplot(fig)

# Summary metrics
total_sales = filtered['Weekly_Sales_Pred'].sum()
mean_sales = filtered['Weekly_Sales_Pred'].mean()

st.metric("Total Forecasted Sales (Selected Range)", f"${total_sales:,.2f}")
st.metric("Average Weekly Sales", f"${mean_sales:,.2f}")

# Optional: Show Data Table
if st.checkbox("Show Raw Data Table"):
    st.dataframe(filtered[['Date', 'Weekly_Sales_Pred']].sort_values('Date'))

# Download CSV
csv = filtered.to_csv(index=False).encode('utf-8')
st.download_button("Download Forecast Data", data=csv, file_name=f"forecast_store{store}_dept{dept}.csv", mime='text/csv')

# Optional: Add heatmap
st.subheader("Sales by Department and Store (Full Test Set)")
pivot = test.pivot_table(index="Dept", columns="Store", values="Weekly_Sales_Pred", aggfunc='sum')
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.heatmap(pivot, cmap="YlGnBu", ax=ax2)
ax2.set_title("Predicted Sales by Department and Store")
st.pyplot(fig2)
