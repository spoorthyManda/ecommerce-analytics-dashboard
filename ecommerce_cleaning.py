import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data.csv', encoding='latin-1')
print("Original shape:", df.shape)

# 1. Drop missing CustomerID
df = df.dropna(subset=['CustomerID'])
print("After dropping missing CustomerID:", df.shape)

# 2. Remove cancelled orders (InvoiceNo starts with C)
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
print("After removing cancellations:", df.shape)

# 3. Remove negative/zero quantity and price
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]
print("After removing invalid quantities/prices:", df.shape)

# 4. Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 5. Extract date features
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['MonthName'] = df['InvoiceDate'].dt.strftime('%b')
df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
df['Hour'] = df['InvoiceDate'].dt.hour

# 6. Create Revenue column
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# 7. Convert CustomerID to integer
df['CustomerID'] = df['CustomerID'].astype(int)

# 8. Reset index
df = df.reset_index(drop=True)

# 9. Save clean data
df.to_csv('ecommerce_clean.csv', index=False)

print("\nClean dataset saved!")
print("Final shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nSample data:")
print(df.head())
print("\nRevenue stats:")
print(df['Revenue'].describe())