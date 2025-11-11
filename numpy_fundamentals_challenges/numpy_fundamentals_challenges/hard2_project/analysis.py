# Hard 2 — Analysis using NumPy end-to-end
# Steps:
# 1) Load CSV -> NumPy
# 2) Compute KPIs (monthly revenue, category mix, top store)
# 3) Save a plot using matplotlib

import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import defaultdict

# ---- 1) Load CSV -> NumPy ----
# We'll parse using csv to emphasize NumPy transformation
dates, stores, cats, qtys, prices, revs = [], [], [], [], [], []
with open("hard2_project/data/sales_2024.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dates.append(row["date"])
        stores.append(row["store"])
        cats.append(row["category"])
        qtys.append(int(row["qty"]))
        prices.append(float(row["price"]))
        revs.append(float(row["revenue"]))

dates  = np.array(dates, dtype="datetime64[D]")
stores = np.array(stores)
cats   = np.array(cats)
qtys   = np.array(qtys, dtype=np.int32)
prices = np.array(prices, dtype=np.float32)
revs   = np.array(revs, dtype=np.float64)

# ---- 2) KPIs with pure NumPy ----
# Monthly revenue
months = dates.astype("datetime64[M]")
uniq_months, month_idx = np.unique(months, return_inverse=True)
monthly_rev = np.bincount(month_idx, weights=revs)

# Category mix
uniq_cats, cat_idx = np.unique(cats, return_inverse=True)
cat_rev = np.bincount(cat_idx, weights=revs)

# Top store by revenue
uniq_stores, store_idx = np.unique(stores, return_inverse=True)
store_rev = np.bincount(store_idx, weights=revs)
top_store = uniq_stores[np.argmax(store_rev)]

print("Unique months:", uniq_months.astype(str))
print("Monthly revenue (first 3):", np.round(monthly_rev[:3], 2))
print("Category revenue:", dict(zip(uniq_cats, np.round(cat_rev, 2))))
print("Top store by revenue:", top_store)

# ---- 3) Plot and save ----
plt.figure(figsize=(8, 4.5))
# x-axis as 0..11, labels from uniq_months
x = np.arange(len(uniq_months))
plt.plot(x, monthly_rev)
plt.xticks(x, uniq_months.astype(str), rotation=45, ha="right")
plt.title("Monthly Revenue — 2024")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("hard2_project/figures/monthly_revenue.png", dpi=160)
print("Saved figure to hard2_project/figures/monthly_revenue.png")
