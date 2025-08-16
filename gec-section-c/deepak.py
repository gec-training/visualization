from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import pandas as pd

# Start Spark Session
spark = SparkSession.builder.appName("Superstore Analysis").getOrCreate()

# Load CSV using Spark
df_spark = spark.read.csv("../dataset/sample-superstore.csv", header=True, inferSchema=True)

# Convert Spark DataFrame to Pandas
df = df_spark.toPandas()

# Fix datatypes
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

# Create subplots
fig, axes = plt.subplots(3, 1, figsize=(12, 15))

# 1. Sales by Product Category
category_sales = df.groupby("Category")["Sales"].sum()
axes[0].bar(category_sales.index, category_sales.values, color="green", edgecolor="black")
axes[0].set_title("Total Sales by Product Category")
axes[0].set_xlabel("Product Category")
axes[0].set_ylabel("Total Sales")
axes[0].tick_params(axis='x', rotation=45)

# 2. Profit vs Sales
axes[1].scatter(df["Sales"], df["Profit"], alpha=0.5, color="purple")
axes[1].set_title("Profit vs Sales")
axes[1].set_xlabel("Sales")
axes[1].set_ylabel("Profit")

# 3. Sales Trend Over Time
sales_trend = df.groupby("Order Date")["Sales"].sum()
axes[2].plot(sales_trend.index, sales_trend.values, color="blue")
axes[2].set_title("Sales Trend Over Time")
axes[2].set_xlabel("Date")
axes[2].set_ylabel("Sales")

# Adjust layout
plt.tight_layout()
plt.show()
