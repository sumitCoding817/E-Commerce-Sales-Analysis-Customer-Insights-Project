
import pandas as pd
from pathlib import Path

# STEP 1: File paths
project_dir = Path(__file__).resolve().parent.parent

input_file = project_dir / "data" / "cleaned_ecommerce_sales.csv"
output_dir = project_dir / "outputs"

output_dir.mkdir(exist_ok=True)

# STEP 2: Load cleaned dataset
df = pd.read_csv(input_file, parse_dates=["Order Date"])

print("\nDataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# STEP 3: Overall Sales Summary
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_quantity = df["Quantity"].sum()

profit_margin = (
    (total_profit / total_sales) * 100
    if total_sales != 0 else 0
)

average_order_value = (
    total_sales / total_orders
    if total_orders != 0 else 0
)

print("\n========== SALES SUMMARY ==========")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Average Order Value: ${average_order_value:.2f}")

# STEP 4: Category-wise Sales and Profit
category_analysis = (
    df.groupby("Category")[["Sales", "Profit"]]
    .sum()
    .sort_values("Sales", ascending=False)
)

print("\n========== CATEGORY ANALYSIS ==========")
print(category_analysis)

category_analysis.to_csv(
    output_dir / "category_analysis.csv"
)

# STEP 5: Region-wise Sales and Profit
region_analysis = (
    df.groupby("Region")[["Sales", "Profit"]]
    .sum()
    .sort_values("Sales", ascending=False)
)

print("\n========== REGION ANALYSIS ==========")
print(region_analysis)

region_analysis.to_csv(
    output_dir / "region_analysis.csv"
)

# STEP 6: Top 10 Products by Revenue
top_products = (
    df.groupby("Product Name")[["Sales", "Profit", "Quantity"]]
    .sum()
    .sort_values("Sales", ascending=False)
    .head(10)
)

print("\n========== TOP 10 PRODUCTS ==========")
print(top_products)

top_products.to_csv(
    output_dir / "top10_products.csv"
)

# STEP 7: Top 10 Customers by Revenue
top_customers = (
    df.groupby(["Customer ID", "Customer Name"])[["Sales", "Profit"]]
    .sum()
    .sort_values("Sales", ascending=False)
    .head(10)
)

print("\n========== TOP 10 CUSTOMERS ==========")
print(top_customers)

top_customers.to_csv(
    output_dir / "top10_customers.csv"
)

# STEP 8: Monthly Sales Trends
df["Year Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Year Month")[["Sales", "Profit"]]
    .sum()
    .sort_index()
)

monthly_sales.index = monthly_sales.index.astype(str)

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

monthly_sales.to_csv(
    output_dir / "monthly_sales.csv"
)

# STEP 9: Loss-Making Products
loss_products = (
    df.groupby("Product Name")[["Sales", "Profit"]]
    .sum()
)

loss_products = (
    loss_products[loss_products["Profit"] < 0]
    .sort_values("Profit")
)

print("\n========== LOSS-MAKING PRODUCTS ==========")
print(loss_products.head(10))

loss_products.to_csv(
    output_dir / "loss_products.csv"
)

# STEP 10: Discount vs Profit Analysis
df["Discount Range"] = pd.cut(
    df["Discount"],
    bins=[-0.001, 0.0, 0.2, 0.4, 0.6, 1.0],
    labels=[
        "No Discount",
        "0-20%",
        "20-40%",
        "40-60%",
        "60-100%"
    ],
    include_lowest=True
)

discount_analysis = (
    df.groupby("Discount Range", observed=True)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Lines=("Sales", "size")
    )
)

print("\n========== DISCOUNT ANALYSIS ==========")
print(discount_analysis)

discount_analysis.to_csv(
    output_dir / "discount_analysis.csv"
)

print("\nAll Sales Analysis Completed Successfully!")
