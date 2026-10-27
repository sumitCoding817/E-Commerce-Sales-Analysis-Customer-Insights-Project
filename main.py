import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('data/ecommerce_sales.csv')

print('\nFirst 5 rows')
print(df.head())

print('\nDataset Shape: ')
print(df.shape)

print('\nColumn Names :')
print(df.columns.to_list())

print('\Data information')
print(df.info())

print('\nMissing values')
print(df.isnull().sum())

print('\nDuplicated Rows')
print(df.duplicated().sum())

print('\nSatatical Summary')
print(df.describe())

total_sales=df['Sales'].sum()
total_profit=df['Profit'].sum()
total_orders=df['Order ID'].unique()
total_customers=df['Customer ID'].nunique()

profit_margin=np.where(
  total_sales !=0,
  (total_profit/total_sales)*100,
  0
)

print("\n========== SALES SUMMARY ==========")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Profit Margin: {float(profit_margin):.2f}%")

category_sales=df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(8,5))

plt.bar(category_sales.index,category_sales.values,color=['skyblue','orange','green'])
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Sales (USD)')
plt.tight_layout()
plt.savefig('outputs/category_sales_product.png')
plt.show()