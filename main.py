import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data_sales.csv")

# Clean data
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Date handling (IMPORTANT FIX)
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create Month column
df["Month"] = df["Order Date"].dt.to_period("M")

# Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()

# Top Products
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)

# Print results
print("Monthly Sales:\n", monthly_sales)
print("\nTop Products:\n", top_products)

# Save insights
with open("outputs/insights.txt", "w") as f:
    f.write("Top Products:\n")
    f.write(str(top_products))

# Plot 1: Monthly Sales
plt.figure()
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.tight_layout()
plt.savefig("outputs/charts/monthly_sales.png")
plt.show()

# Plot 2: Top Products
plt.figure()
top_products.plot(kind="bar")
plt.title("Top Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("outputs/charts/top_products.png")
plt.show()