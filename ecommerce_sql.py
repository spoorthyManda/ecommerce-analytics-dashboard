import pandas as pd
import sqlite3

df = pd.read_csv('ecommerce_clean.csv')
conn = sqlite3.connect('ecommerce.db')
df.to_sql('orders', conn, if_exists='replace', index=False)
print("Data loaded into SQLite!")

# Query 1 — Total Revenue & Orders
print("\nBusiness Overview:")
q1 = pd.read_sql_query("""
    SELECT
        COUNT(DISTINCT InvoiceNo) AS total_orders,
        COUNT(DISTINCT CustomerID) AS total_customers,
        ROUND(SUM(Revenue), 2) AS total_revenue,
        ROUND(AVG(Revenue), 2) AS avg_order_value
    FROM orders
""", conn)
print(q1)

# Query 2 — Revenue by Country
print("\nTop 10 Countries by Revenue:")
q2 = pd.read_sql_query("""
    SELECT Country,
           ROUND(SUM(Revenue), 2) AS total_revenue,
           COUNT(DISTINCT CustomerID) AS customers,
           COUNT(DISTINCT InvoiceNo) AS orders
    FROM orders
    GROUP BY Country
    ORDER BY total_revenue DESC
    LIMIT 10
""", conn)
print(q2)

# Query 3 — Monthly Revenue
print("\nMonthly Revenue:")
q3 = pd.read_sql_query("""
    SELECT Year, Month, MonthName,
           ROUND(SUM(Revenue), 2) AS monthly_revenue,
           COUNT(DISTINCT InvoiceNo) AS orders
    FROM orders
    GROUP BY Year, Month
    ORDER BY Year, Month
""", conn)
print(q3)

# Query 4 — Top 10 Products
print("\nTop 10 Products by Revenue:")
q4 = pd.read_sql_query("""
    SELECT Description,
           ROUND(SUM(Revenue), 2) AS total_revenue,
           SUM(Quantity) AS total_quantity
    FROM orders
    GROUP BY Description
    ORDER BY total_revenue DESC
    LIMIT 10
""", conn)
print(q4)

# Query 5 — Top 10 Customers
print("\nTop 10 Customers:")
q5 = pd.read_sql_query("""
    SELECT CustomerID,
           Country,
           ROUND(SUM(Revenue), 2) AS total_revenue,
           COUNT(DISTINCT InvoiceNo) AS total_orders
    FROM orders
    GROUP BY CustomerID
    ORDER BY total_revenue DESC
    LIMIT 10
""", conn)
print(q5)

conn.close()
print("\nAll SQL queries complete!")