
import streamlit as st
import pandas as pd
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Afficionado Coffee Sales Dashboard",
    page_icon="☕",
    layout="wide"
)

# Load dataset
file_path = (
    Path(__file__).resolve().parent.parent
    / "report"
    / "afficionado_cleaned_dataset.csv"
)

df = pd.read_csv(file_path)

# Dashboard title
st.title("☕ Afficionado Coffee Roasters")
st.subheader("Sales Trend and Time-Based Performance Analysis")
st.markdown("---")

# Key Performance Indicators
total_revenue = df["revenue"].sum()
total_transactions = df["transaction_id"].nunique()
total_quantity = df["transaction_qty"].sum()
average_order_value = total_revenue / total_transactions

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Transactions", f"{total_transactions:,}")
col3.metric("Products Sold", f"{total_quantity:,}")
col4.metric("Average Transaction Value", f"${average_order_value:.2f}")

st.markdown("---")


# Interactive Filters
st.header("Dashboard Filters")

col1, col2 = st.columns(2)

with col1:
    selected_store = st.multiselect(
    "Select Store",
    options=sorted(df["store_location"].unique()),
    default=sorted(df["store_location"].unique()),
    key="store_filter"
)

with col2:
    selected_category = st.multiselect(
    "Select Product Category",
    options=sorted(df["product_category"].unique()),
    default=sorted(df["product_category"].unique()),
    key="category_filter"
)

filtered_df = df[
    (df["store_location"].isin(selected_store)) &
    (df["product_category"].isin(selected_category))
]



# Store performance
st.header("Store Performance")

store_sales = filtered_df.groupby("store_location")["revenue"].sum().sort_values(
    ascending=False
)
st.bar_chart(store_sales)

# Category performance
st.header("Product Category Performance")

category_sales = filtered_df.groupby("product_category")["revenue"].sum().sort_values(
    ascending=False
)

st.bar_chart(category_sales)

# Hourly sales
st.header("Hourly Sales Performance")

hourly_sales = (
    filtered_df.groupby("transaction_hour")["revenue"]
    .sum()
    .reindex(range(24), fill_value=0)
)

st.line_chart(hourly_sales)

# Time period analysis
st.header("Revenue by Time Period")

time_sales = filtered_df.groupby("time_period", observed=False)["revenue"].sum()

st.bar_chart(time_sales)

# Detailed data
# Business Insights
st.markdown("---")
st.header("Business Insights")

if not filtered_df.empty:
    best_store = (
        filtered_df.groupby("store_location")["revenue"]
        .sum().idxmax()
    )

    best_category = (
        filtered_df.groupby("product_category")["revenue"]
        .sum().idxmax()
    )

    peak_hour = (
        filtered_df.groupby("transaction_hour")["revenue"]
        .sum().idxmax()
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Top Performing Store", best_store)
    col2.metric("Top Revenue Category", best_category)
    col3.metric("Peak Sales Hour", f"{peak_hour}:00")
else:
    st.info("No sales data available for the selected filters.")
# Business Recommendations
st.markdown("---")
st.header("Business Recommendations")

st.write("""
1. **Focus on Peak Hours:** Ensure sufficient staff and inventory
   during high-revenue hours.

2. **Promote Top Categories:** Prioritize high-performing product
   categories through targeted promotions.

3. **Improve Store Performance:** Study sales patterns across
   locations to identify opportunities for improvement.

4. **Optimize Product Availability:** Maintain adequate stock
   of popular products to meet customer demand.

5. **Use Data-Driven Decisions:** Monitor sales KPIs regularly
   to improve operational efficiency and profitability.
""")
# Download Filtered Sales Report
st.markdown("---")
st.header("Download Sales Report")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Sales Data (CSV)",
    data=csv_data,
    file_name="afficionado_filtered_sales_report.csv",
    mime="text/csv"
)
st.header("Sales Data Preview")
st.dataframe(filtered_df.head(20), use_container_width=True)
st.success("Sales dashboard loaded successfully!")
