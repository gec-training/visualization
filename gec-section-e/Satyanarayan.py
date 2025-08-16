import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\satya\PycharmProjects\visualization\dataset\sample-superstore.csv")

# Create figure with extra space at the top
fig, axes = plt.subplots(2, 3, figsize=(18, 9))

# Add Super Title (Dashboard Heading) with enough margin
plt.subplots_adjust(top=0.82, hspace=0.6, wspace=0.4, left=0.07, right=0.95)
fig.suptitle("Superstore Sales & Profit Dashboard",
             fontsize=20, weight="bold", y=0.98)

# ------------------------------
# 1. Sales & Profit by Product Category
category_group = df.groupby("Product Category")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False)
x = range(len(category_group))
axes[0,0].bar(x, category_group["Sales"], width=0.4, label="Sales", color="skyblue")
axes[0,0].bar([i+0.4 for i in x], category_group["Profit"], width=0.4, label="Profit", color="lightgreen")
axes[0,0].set_title("Sales & Profit by Category", fontsize=11, weight="bold")
axes[0,0].set_xticks([i+0.2 for i in x])
axes[0,0].set_xticklabels(category_group.index, rotation=15, fontsize=9)
axes[0,0].legend(fontsize=8)

# ------------------------------
# 2. Sales & Profit by Region
region_group = df.groupby("Region")[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False)
x = range(len(region_group))
axes[0,1].bar(x, region_group["Sales"], width=0.4, label="Sales", color="orange")
axes[0,1].bar([i+0.4 for i in x], region_group["Profit"], width=0.4, label="Profit", color="seagreen")
axes[0,1].set_title("Sales & Profit by Region", fontsize=11, weight="bold")
axes[0,1].set_xticks([i+0.2 for i in x])
axes[0,1].set_xticklabels(region_group.index, rotation=15, fontsize=9)
axes[0,1].legend(fontsize=8)

# ------------------------------
# 3. Sales vs Discount (Colored by Profit)
sc = axes[0,2].scatter(df["Discount"], df["Sales"], c=df["Profit"], cmap="coolwarm", alpha=0.6, edgecolor="k", s=25)
axes[0,2].set_title("Sales vs Discount", fontsize=11, weight="bold")
axes[0,2].set_xlabel("Discount", fontsize=9)
axes[0,2].set_ylabel("Sales", fontsize=9)
cbar = fig.colorbar(sc, ax=axes[0,2], shrink=0.8)
cbar.set_label("Profit", fontsize=9)

# ------------------------------
# 4. Top 10 Profitable Products
top_products = df.groupby("Product Name")[["Profit"]].sum().sort_values("Profit", ascending=False).head(10)
bars = axes[1,1].barh(top_products.index, top_products["Profit"], color="salmon")
axes[1,1].bar_label(bars, fmt="%.0f", fontsize=8)
axes[1,1].set_title("Top 10 Profitable Products", fontsize=11, weight="bold")
axes[1,1].tick_params(axis="y", labelsize=8)
axes[1,1].invert_yaxis()

# ------------------------------
# 5. Sales & Profit by Customer Segment
segment_group = df.groupby("Customer Segment")[["Sales", "Profit"]].sum()
x = range(len(segment_group))
axes[1,2].bar(x, segment_group["Sales"], width=0.4, label="Sales", color="dodgerblue")
axes[1,2].bar([i+0.4 for i in x], segment_group["Profit"], width=0.4, label="Profit", color="limegreen")
axes[1,2].set_title("Sales & Profit by Segment", fontsize=11, weight="bold")
axes[1,2].set_xticks([i+0.2 for i in x])
axes[1,2].set_xticklabels(segment_group.index, fontsize=9)
axes[1,2].legend(fontsize=8)

# ------------------------------
# Remove unused bottom-left subplot
fig.delaxes(axes[1,0])

plt.show()