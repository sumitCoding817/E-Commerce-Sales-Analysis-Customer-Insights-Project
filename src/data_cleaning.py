import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
input_file=project_dir/"data"/"ecommerce_sales.csv"
output_file=project_dir/"data"/"cleaned_ecommerce_sales.csv"

df=pd.read_csv(input_file,encoding='utf-8')

print("Original Dataset Shape : ",df.shape)

print('\nMissing Values :')
print(df.isnull().sum())

df=df.drop_duplicates().copy()

required_column=['Order ID','Order Date','Ship Date','Sales','Profit','Quantity','Discount']

df=df.dropna(subset=required_column).copy()

df['Order Date']=pd.to_datetime(
  df['Order Date'],format='mixed',dayfirst=False,errors='coerce'
)

df['Ship Date']=pd.to_datetime(
  df['Ship Date'],format='mixed',dayfirst=False, errors='coerce'
)

df=df.dropna(subset=['Order Date','Ship Date']).copy()

numeric_column=['Sales','Profit','Quantity','Discount']

for col in numeric_column:
  df[col]=pd.to_numeric(df[col],errors='coerce')

df=df.dropna(subset=numeric_column).copy()

df["Profit Margin"] = (
    df["Profit"] / df["Sales"].replace(0, float("nan"))
) * 100

df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()

df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

df.to_csv(output_file, index=False)

print("\nCleaned Dataset Shape:", df.shape)
print("\nNew Columns:")
print(df[[
    "Order Year", "Order Month",
    "Month Name", "Profit Margin",
    "Shipping Days"
]].head())

print("\nData Cleaning Completed Successfully!")
print("Saved File:", output_file)