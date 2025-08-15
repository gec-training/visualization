import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 1. Load CSV with Pandas
file_path = r"C:/Users/LENOVO/Desktop/Big_Data_Analysis_GEC/visualization-BDA-fork/dataset/sample-superstore.csv"
df = pd.read_csv(file_path)

# 2. Group by Product Category
category_stats = (
    df.groupby("Product Category")[["Profit", "Sales", "Quantity ordered new"]]
    .sum()
    .sort_values("Profit")
)

# 3. Plot
plt.style.use("seaborn-v0_8-darkgrid")
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# --- Profit Chart ---
bars1 = axes[0].bar(category_stats.index, category_stats["Profit"],
                    color=["#ff9999", "#66b3ff", "#99ff99"])
axes[0].set_title("Total Profit by Category", fontsize=14, fontweight="bold")
axes[0].yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x:,.0f}"))
for bar in bars1:
    axes[0].annotate(f"${bar.get_height():,.0f}", 
                     xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                     xytext=(0, 5), textcoords="offset points", 
                     ha='center', fontsize=9)

# --- Sales Chart ---
bars2 = axes[1].bar(category_stats.index, category_stats["Sales"],
                    color=["#66b3ff", "#99ff99", "#ff9999"])
axes[1].set_title("Total Sales by Category", fontsize=14, fontweight="bold")
axes[1].yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x:,.0f}"))
for bar in bars2:
    axes[1].annotate(f"${bar.get_height():,.0f}", 
                     xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                     xytext=(0, 5), textcoords="offset points", 
                     ha='center', fontsize=9)

# --- Quantity Chart ---
bars3 = axes[2].bar(category_stats.index, category_stats["Quantity ordered new"],
                    color=["#99ff99", "#ff9999", "#66b3ff"])
axes[2].set_title("Total Quantity by Category", fontsize=14, fontweight="bold")
for bar in bars3:
    axes[2].annotate(f"{bar.get_height():,.0f}", 
                     xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                     xytext=(0, 5), textcoords="offset points", 
                     ha='center', fontsize=9)

# Formatting
for ax in axes:
    ax.set_xticklabels(category_stats.index, rotation=15)

plt.tight_layout()
plt.savefig("category_analysis_simple.png", dpi=300)
plt.show()
