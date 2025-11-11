# Hard 2 — Mini Project: Retail Sales Analytics (Synthetic)
# Create a 12-month dataset of daily transactions for 5 stores and 3 product categories.
# Uses only stdlib (csv) + numpy to avoid extra dependencies.

import numpy as np
import csv

rng = np.random.default_rng(7)

days = np.arange("2024-01-01", "2024-12-31", dtype="datetime64[D]")
stores = np.array([f"S{i}" for i in range(1,6)])
cats   = np.array(["A", "B", "C"])

with open("hard2_project/data/sales_2024.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "store", "category", "qty", "price", "revenue"])
    count = 0
    for d in days:
        # base demand with weekly seasonality
        dow = (np.datetime64(d) - np.datetime64("1970-01-01")).astype("timedelta64[D]").astype(int) % 7
        weekday_boost = 1.0 + 0.15*np.sin(2*np.pi*dow/7)
        month = int(str(d)[5:7])
        season = 1.0 + 0.25*np.sin(2*np.pi*(month-1)/12)
        for s in stores:
            for c in cats:
                price = {"A": 20.0, "B": 35.0, "C": 12.0}[c]
                base_mu = {"A": 40, "B": 22, "C": 70}[c]
                qty = rng.poisson(lam=base_mu * season * weekday_boost)
                revenue = float(qty) * float(price)
                writer.writerow([str(d), s, c, int(qty), float(price), revenue])
                count += 1

print("Wrote hard2_project/data/sales_2024.csv with", count, "rows.")
