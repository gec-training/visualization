import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 1. Load CSV with Pandas
file_path = r"C:/Users/SOHAM/Desktop/visualization/dataset/sample-superstore.csv"
df = pd.read_csv(file_path)

# 2. Group by Product Category
category_stats = (
    df.groupby("Product Category")[["Profit", "Sales", "Quantity ordered new"]]
    .sum()
    .sort_values("Profit", ascending=False)
)

# 3. Plot
plt.style.use("seaborn-v0_8-whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(18, 5), facecolor="#f9fafb")

colors = ["#4f8bc9", "#a3c585", "#f7b267"]

# --- Profit Chart ---
bars1 = axes[0].bar(category_stats.index, category_stats["Profit"], color=colors)
axes[0].set_title("Profit by Category", fontsize=14, fontweight="bold")
axes[0].yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x:,.0f}"))
for bar in bars1:
    height = bar.get_height()
    axes[0].annotate(f"${height:,.0f}", 
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 6), textcoords="offset points", 
                     ha='center', va='bottom', fontsize=10, fontweight='bold', color="#333")

# --- Sales Chart ---
bars2 = axes[1].bar(category_stats.index, category_stats["Sales"], color=colors)
axes[1].set_title("Sales by Category", fontsize=14, fontweight="bold")
axes[1].yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x:,.0f}"))
for bar in bars2:
    height = bar.get_height()
    axes[1].annotate(f"${height:,.0f}", 
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 6), textcoords="offset points", 
                     ha='center', va='bottom', fontsize=10, fontweight='bold', color="#333")

# --- Quantity Chart ---
bars3 = axes[2].bar(category_stats.index, category_stats["Quantity ordered new"], color=colors)
axes[2].set_title("Quantity by Category", fontsize=14, fontweight="bold")
for bar in bars3:
    height = bar.get_height()
    axes[2].annotate(f"{height:,.0f}", 
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 6), textcoords="offset points", 
                     ha='center', va='bottom', fontsize=10, fontweight='bold', color="#333")

# Formatting
for ax in axes:
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xticklabels(category_stats.index, rotation=15, fontsize=11)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.subplots_adjust(wspace=0.25)
plt.tight_layout()
plt.savefig("category_analysis_clean.png", dpi=300, facecolor="#f9fafb")
plt.show()