import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (change filename if needed)
df = pd.read_csv("../dataset/sample-superstore.csv")

# ------------------------------
# Example 1: Sales by Category
# ------------------------------
if "Category" in df.columns and "Sales" in df.columns:
    category_sales = df.groupby("Category")["Sales"].sum()

    plt.figure(figsize=(8, 6))
    category_sales.plot(kind="bar", color=["skyblue", "orange", "green"])
    plt.title("Total Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ------------------------------
# Example 2: Sales by Region
# ------------------------------
if "Region" in df.columns and "Sales" in df.columns:
    region_sales = df.groupby("Region")["Sales"].sum()

    plt.figure(figsize=(6, 6))
    region_sales.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Sales Distribution by Region")
    plt.ylabel("")  # hide y-axis label
    plt.tight_layout()
    plt.show()

# ------------------------------
# Example 3: Sales Trend Over Time
# ------------------------------
if "Order Date" in df.columns and "Sales" in df.columns:
    # Convert to datetime
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Year"] = df["Order Date"].dt.year

    yearly_sales = df.groupby("Year")["Sales"].sum()

    plt.figure(figsize=(8, 6))
    yearly_sales.plot(kind="line", marker="o", color="purple")
    plt.title("Yearly Sales Trend")
    plt.xlabel("Year")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
