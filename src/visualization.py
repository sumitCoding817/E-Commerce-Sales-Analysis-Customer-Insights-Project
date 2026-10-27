
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# File paths
project_dir = Path(__file__).resolve().parent.parent
output_dir = project_dir / "outputs"

# Load analysis files
category = pd.read_csv(output_dir / "category_analysis.csv")
region = pd.read_csv(output_dir / "region_analysis.csv")
products = pd.read_csv(output_dir / "top10_products.csv")
customers = pd.read_csv(output_dir / "top10_customers.csv")
monthly = pd.read_csv(output_dir / "monthly_sales.csv")
loss = pd.read_csv(output_dir / "loss_products.csv")
discount = pd.read_csv(output_dir / "discount_analysis.csv")

# GRAPH 1: Category-wise Sales
plt.figure(figsize=(8, 5))
plt.bar(category["Category"], category["Sales"],
        color=["skyblue", "orange", "green"])
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales (USD)")
plt.tight_layout()
plt.savefig(output_dir / "category_sales.png")
plt.show()

# GRAPH 2: Region-wise Profit
plt.figure(figsize=(8, 5))
plt.bar(region["Region"], region["Profit"],
        color="teal")
plt.title("Region-wise Profit")
plt.xlabel("Region")
plt.ylabel("Profit (USD)")
plt.tight_layout()
plt.savefig(output_dir / "region_profit.png")
plt.show()

# GRAPH 3: Top 10 Products by Sales
plt.figure(figsize=(10, 6))
plt.barh(products["Product Name"], products["Sales"],
         color="purple")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Sales (USD)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(output_dir / "top10_products.png")
plt.show()

# GRAPH 4: Top 10 Customers
plt.figure(figsize=(10, 6))
plt.barh(customers["Customer Name"], customers["Sales"],
         color="steelblue")
plt.title("Top 10 Customers by Revenue")
plt.xlabel("Sales (USD)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(output_dir / "top10_customers.png")
plt.show()

# GRAPH 5: Monthly Sales Trend
plt.figure(figsize=(12, 5))
plt.plot(monthly["Year Month"], monthly["Sales"],
         color="blue", marker="o", markersize=3)
plt.title("Monthly Sales Trend")
plt.xlabel("Year-Month")
plt.ylabel("Sales (USD)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(output_dir / "monthly_sales.png")
plt.show()

# GRAPH 6: Monthly Profit Trend
plt.figure(figsize=(12, 5))
plt.plot(monthly["Year Month"], monthly["Profit"],
         color="green", marker="o", markersize=3)
plt.title("Monthly Profit Trend")
plt.xlabel("Year-Month")
plt.ylabel("Profit (USD)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(output_dir / "monthly_profit.png")
plt.show()

# GRAPH 7: Top 10 Loss-Making Products
top_loss = loss.head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_loss["Product Name"], top_loss["Profit"],
         color="red")
plt.title("Top 10 Loss-Making Products")
plt.xlabel("Profit / Loss (USD)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(output_dir / "loss_products.png")
plt.show()

# GRAPH 8: Discount vs Profit
plt.figure(figsize=(9, 5))
plt.bar(discount["Discount Range"].astype(str),
        discount["Total_Profit"], color="orange")
plt.title("Profit by Discount Range")
plt.xlabel("Discount Range")
plt.ylabel("Total Profit (USD)")
plt.tight_layout()
plt.savefig(output_dir / "discount_profit.png")
plt.show()

print("All 8 Visualizations Generated Successfully!")
