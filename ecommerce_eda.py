import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_clean.csv')
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Chart 1 — Monthly Revenue Trend
monthly = df.groupby(['Year', 'Month'])['Revenue'].sum().reset_index()
monthly['Period'] = monthly['Year'].astype(str) + '-' + monthly['Month'].astype(str).str.zfill(2)
plt.figure()
plt.plot(monthly['Period'], monthly['Revenue'], marker='o', color='#1a1a2e', linewidth=2)
plt.fill_between(range(len(monthly)), monthly['Revenue'], alpha=0.1, color='#1a1a2e')
plt.xticks(range(len(monthly)), monthly['Period'], rotation=45)
plt.title('Monthly Revenue Trend', fontsize=14)
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.savefig('chart1_monthly_revenue.png')
plt.show()
print("Chart 1 saved!")

# Chart 2 — Top 10 Countries by Revenue
top_countries = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(10)
plt.figure()
sns.barplot(x=top_countries.values, y=top_countries.index, palette='Blues_r')
plt.title('Top 10 Countries by Revenue', fontsize=14)
plt.xlabel('Total Revenue ($)')
plt.tight_layout()
plt.savefig('chart2_top_countries.png')
plt.show()
print("Chart 2 saved!")

# Chart 3 — Revenue by Day of Week
dow_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
dow = df.groupby('DayOfWeek')['Revenue'].sum().reindex(dow_order)
plt.figure()
sns.barplot(x=dow.index, y=dow.values, palette='Blues_r')
plt.title('Revenue by Day of Week', fontsize=14)
plt.ylabel('Total Revenue ($)')
plt.tight_layout()
plt.savefig('chart3_day_of_week.png')
plt.show()
print("Chart 3 saved!")

# Chart 4 — Top 10 Products by Revenue
top_products = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)
plt.figure()
sns.barplot(x=top_products.values, y=top_products.index, palette='Blues_r')
plt.title('Top 10 Products by Revenue', fontsize=14)
plt.xlabel('Total Revenue ($)')
plt.tight_layout()
plt.savefig('chart4_top_products.png')
plt.show()
print("Chart 4 saved!")

print("\nAll charts saved!")