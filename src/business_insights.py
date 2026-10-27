
import pandas as pd
from pathlib import Path

# STEP 1: File paths
project_dir = Path(__file__).resolve().parent.parent

input_file = project_dir / "data" / "cleaned_ecommerce_sales.csv"
output_dir = project_dir / "outputs"

output_dir.mkdir(exist_ok=True)

# STEP 2: Load dataset
df = pd.read_csv(
    input_file,
    parse_dates=["Order Date"]
)

# STEP 3: Overall business performance
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0 else 0
)

average_order_value = (
    total_sales / total_orders
    if total_orders != 0 else 0
)

# STEP 4: Category performance
category = df.groupby("Category")[["Sales", "Profit"]].sum()

best_category = category["Sales"].idxmax()
best_category_sales = category.loc[best_category, "Sales"]

# STEP 5: Region performance
region = df.groupby("Region")[["Sales", "Profit"]].sum()

best_region = region["Profit"].idxmax()
best_region_profit = region.loc[best_region, "Profit"]

# STEP 6: Top product
products = df.groupby("Product Name")["Sales"].sum()

top_product = products.idxmax()
top_product_sales = products.max()

# STEP 7: Top customer
customers = (
    df.groupby(["Customer ID", "Customer Name"])["Sales"]
    .sum()
)

top_customer = customers.idxmax()
top_customer_sales = customers.max()

# STEP 8: Monthly sales
df["Year Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Year Month")["Sales"].sum()

best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

# STEP 9: Loss-making products
product_profit = df.groupby("Product Name")["Profit"].sum()

loss_products = product_profit[product_profit < 0]

loss_count = len(loss_products)
total_product_loss = loss_products.sum()

# STEP 10: Business recommendations
recommendations = []

if profit_margin < 10:
    recommendations.append(
        "Review pricing and costs because overall profit margin is below 10%."
    )
else:
    recommendations.append(
        "Maintain profitability and monitor changes in product margins."
    )

if loss_count > 0:
    recommendations.append(
        f"Investigate {loss_count} loss-making products and review their discounts and costs."
    )

recommendations.append(
    f"Study the factors behind strong sales in the {best_category} category."
)

recommendations.append(
    f"Review successful practices in the {best_region} region."
)

# STEP 11: Generate report
report = f"""
========================================
       E-COMMERCE SALES REPORT
========================================

1. OVERALL PERFORMANCE
----------------------------------------
Total Revenue       : ${total_sales:,.2f}
Total Profit        : ${total_profit:,.2f}
Total Orders        : {total_orders}
Total Customers     : {total_customers}
Profit Margin       : {profit_margin:.2f}%
Average Order Value : ${average_order_value:,.2f}

2. BEST PRODUCT CATEGORY
----------------------------------------
Category : {best_category}
Revenue  : ${best_category_sales:,.2f}

3. MOST PROFITABLE REGION
----------------------------------------
Region : {best_region}
Profit : ${best_region_profit:,.2f}

4. TOP PRODUCT BY REVENUE
----------------------------------------
Product : {top_product}
Revenue : ${top_product_sales:,.2f}

5. TOP CUSTOMER BY REVENUE
----------------------------------------
Customer : {top_customer[1]}
Customer ID : {top_customer[0]}
Revenue : ${top_customer_sales:,.2f}

6. HIGHEST SALES MONTH
----------------------------------------
Month   : {best_month}
Revenue : ${best_month_sales:,.2f}

7. LOSS-MAKING PRODUCTS
----------------------------------------
Number of Products : {loss_count}
Combined Net Loss  : ${abs(total_product_loss):,.2f}

8. BUSINESS RECOMMENDATIONS
----------------------------------------
"""

for i, recommendation in enumerate(recommendations, start=1):
    report += f"{i}. {recommendation}\n"

report += "\n========================================\n"

# STEP 12: Save report
report_file = output_dir / "business_report.txt"

report_file.write_text(report, encoding="utf-8")

print(report)
print(f"\nReport saved successfully: {report_file}")
