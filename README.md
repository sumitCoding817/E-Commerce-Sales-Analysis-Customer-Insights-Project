# E-Commerce Sales Analysis & Customer Insights

## Project Overview

This project analyzes an e-commerce sales dataset using Python, Pandas, NumPy, and Matplotlib. It focuses on sales performance, profitability, customer behavior, product performance, and business insights.

The project demonstrates an end-to-end data analytics workflow, from data cleaning to visualization and automated reporting.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Visual Studio Code
- Git and GitHub

## Dataset

**Dataset:** Sample Superstore Sales Dataset

**Source:** [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

The dataset contains approximately 9,994 transaction line items with information about orders, products, customers, regions, sales, discounts, and profit.

This is an educational sample dataset, not actual transactions from a live e-commerce company.

## Project Features

### Data Cleaning
- Identified missing values and duplicate records.
- Converted date and numerical columns.
- Created new features such as profit margin, order month, order year, and shipping days.

### Sales Analysis
- Total revenue and profit
- Profit margin and average order value
- Category-wise and region-wise performance
- Top 10 products and customers
- Monthly sales and profit trends
- Loss-making products
- Discount-based profitability analysis

### Data Visualization

Eight visualizations are included:

1. Category-wise Sales
2. Region-wise Profit
3. Top 10 Products by Revenue
4. Top 10 Customers by Revenue
5. Monthly Sales Trend
6. Monthly Profit Trend
7. Top 10 Loss-Making Products
8. Profit by Discount Range

### Business Insights

The project includes an automated text report summarizing key performance indicators, top-performing categories, profitable regions, customers, products, and areas requiring further investigation.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/E-Commerce-Sales-Analysis.git
cd E-Commerce-Sales-Analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download the Sample Superstore dataset and save it as:

`data/ecommerce_sales.csv`

## How to Run

Run the scripts in the following order:

```bash
python src/data_cleaning.py
python src/sales_analysis.py
python src/visualization.py
python src/business_insights.py
```

The generated charts and business report will be available in the `outputs/` directory.

## Learning Outcomes

- Data cleaning and preprocessing using Pandas
- Exploratory Data Analysis (EDA)
- Data aggregation and grouping
- Feature engineering
- Business KPI calculation
- Data visualization using Matplotlib
- Automated reporting
- Interpreting business performance

## Future Improvements

- Interactive dashboard using Streamlit
- SQL-based analysis
- Power BI dashboard
- Customer segmentation
- Sales forecasting

## Author

Sumit Kumar

Computer Science Student | Python & Data Analytics
