# Afficionado Coffee Roasters

## Sales Trend and Time-Based Performance Analysis

### Project Overview
This project analyzes 149,116 sales transactions from Afficionado Coffee Roasters to understand revenue performance, product category performance, store performance, and time-based sales patterns.

The project uses Python for data analysis and Streamlit to build an interactive dashboard.

### Business Objectives
- Evaluate overall sales performance.
- Identify top-performing store locations.
- Analyze revenue across product categories.
- Identify peak sales hours and time periods.
- Generate data-driven business recommendations.

### Dataset Overview
- Total Records: 149,116 transactions
- Year: 2025
- Store Locations: 3
- Product Categories: 9
- Unique Products: 80
- Original Columns: 11

### Tools and Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Streamlit

### Key Performance Indicators
| Metric | Result |
|---|---:|
| Total Revenue | $698,812.33 |
| Total Transactions | 149,116 |
| Products Sold | 214,470 |
| Average Transaction Value | $4.69 |
| Unique Products | 80 |
| Product Categories | 9 |
| Store Locations | 3 |

### Key Findings
- Hell's Kitchen generated the highest revenue.
- Coffee was the highest-revenue product category.
- 10:00 AM was the peak revenue hour.
- Morning sales contributed 55.56% of total revenue.
- Afternoon sales contributed 29.30%.
- Evening sales contributed 15.14%.

### Dashboard Features
- Interactive store and product category filters.
- KPI cards.
- Store performance analysis.
- Product category revenue analysis.
- Hourly sales performance.
- Revenue by time period.
- Business insights and recommendations.
- Filtered sales data preview.
- CSV download functionality.

### Project Structure
```text
Afficionado_Coffee_Analysis/
├── Afficionado Coffee Roasters.xlsx
├── dashboard/
│   └── app.py
├── notebook/
│   └── Afficionado_Coffee_Analysis.ipynb
├── report/
│   ├── afficionado_cleaned_dataset.csv
│   ├── project_kpi_summary.csv
│   ├── project_key_findings.txt
│   └── Afficionado_Coffee_Project_Report.pdf
├── visualization/
│   └── Charts and visualizations
└── README.md
```

### How to Run the Dashboard
1. Install the required packages:
   `pip install pandas streamlit`
2. Navigate to the project folder:
   `cd ~/Projects/Afficionado_Coffee_Analysis`
3. Run the dashboard:
   `streamlit run dashboard/app.py`

### Scope and Limitations
The dataset contains transactions from 2025 and includes transaction time but does not contain a transaction date. Therefore, this project focuses on time-of-day and store-level sales analysis rather than monthly or year-over-year trends.

### Conclusion
This project demonstrates how data analytics and interactive visualization can transform raw retail transaction data into meaningful business insights and support data-driven business decisions.