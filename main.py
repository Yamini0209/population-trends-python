import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------- 1. Create and load sample data ----------
data = {
 "Country": ["India", "India", "India",
 "USA", "USA", "USA",
 "China", "China", "China",
 "Japan", "Japan", "Japan",
 "Brazil", "Brazil", "Brazil",
 "Germany", "Germany", "Germany"],
 "Year": [1960, 1990, 2020] * 6,
 "Population": [
 450000000, 870000000, 1380000000,
 180000000, 250000000, 331000000,
 667000000, 1140000000, 1410000000,
 94000000, 123000000, 126000000,
 72000000, 150000000, 213000000,
 73000000, 79000000, 83000000
 ]
}
df = pd.DataFrame(data)
df.to_csv("population_data.csv", index=False)
df = pd.read_csv("population_data.csv")

print("First five rows:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())

# ---------- 2. Clean and reshape data ----------
df = df.dropna()
df["Population_M"] = df["Population"] / 1_000_000
pivot = df.pivot(index="Year", columns="Country", values="Population_M")
growth_rate = pivot.pct_change() * 100
latest = pivot.loc[2020].sort_values(ascending=False)
share_2020 = latest / latest.sum() * 100

os.makedirs("plots", exist_ok=True)

# ---------- Plot 1: Line chart ----------
plt.figure(figsize=(9, 5))
for country in pivot.columns:
 plt.plot(pivot.index, pivot[country], marker="o", label=country)
plt.title("Population Growth of Selected Countries (1960-2020)")
plt.xlabel("Year")
plt.ylabel("Population (millions)")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("plots/01_line_trend.png", dpi=150)
plt.show()
plt.close()

# ---------- Plot 2: Bar chart for 2020 ----------
plt.figure(figsize=(8, 5))
plt.bar(latest.index, latest.values)
plt.title("Population by Country in 2020")
plt.xlabel("Country")
plt.ylabel("Population (millions)")
for i, value in enumerate(latest.values):
 plt.text(i, value + 15, f"{value:.0f}", ha="center")
plt.tight_layout()
plt.savefig("plots/02_bar_2020.png", dpi=150)
plt.show()
plt.close()

# ---------- Plot 3: Stacked area chart ----------
plt.figure(figsize=(9, 5))
plt.stackplot(pivot.index, pivot.T.values, labels=pivot.columns, alpha=0.85)
plt.title("Cumulative Population of Selected Countries")
plt.xlabel("Year")
plt.ylabel("Population (millions)")
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig("plots/03_stacked_area.png", dpi=150)
plt.show()
plt.close()

# ---------- Plot 4: Growth-rate heatmap ----------
g = growth_rate.dropna()
fig, ax = plt.subplots(figsize=(9, 4))
im = ax.imshow(g.T.values, aspect="auto")
ax.set_xticks(range(len(g.index)))
ax.set_xticklabels(g.index)
ax.set_yticks(range(len(g.columns)))
ax.set_yticklabels(g.columns)
for i in range(g.shape[1]):
 for j in range(g.shape[0]):
  ax.text(j, i, f"{g.T.values[i, j]:.1f}", ha="center",
  va="center", fontsize=8)
plt.colorbar(im, ax=ax, label="Growth (%)")
ax.set_title("Population Growth Between Selected Years (%)")
plt.tight_layout()
plt.savefig("plots/04_growth_heatmap.png", dpi=150)
plt.show()
plt.close()

# ---------- Plot 5: Pie chart for population share in 2020 ----------
plt.figure(figsize=(6.5, 6.5))
plt.pie(share_2020.values, labels=share_2020.index,
 autopct="%1.1f%%", startangle=140)
plt.title("Share of Combined Population, 2020")
plt.tight_layout()
plt.savefig("plots/05_pie_share.png", dpi=150)
plt.show()
plt.close()

# ---------- Plot 6: Population index (1960 = 100) ----------
index_1960 = pivot / pivot.loc[1960] * 100
fig, axes = plt.subplots(2, 3, figsize=(11, 6), sharex=True)
for ax, country in zip(axes.ravel(), index_1960.columns):
 ax.plot(index_1960.index, index_1960[country], marker="o")
 ax.set_title(country)
 ax.set_xlabel("Year")
 ax.set_ylabel("Index")
 ax.grid(alpha=0.3)
fig.suptitle("Population Index (1960 = 100)")
plt.tight_layout()
plt.savefig("plots/06_index_subplots.png", dpi=150)
plt.show()
plt.close()

print("\nFastest growing country from 1960 to 2020:")
print((pivot.loc[2020] / pivot.loc[1960]).idxmax())
print("All six plots saved in the plots folder.")
