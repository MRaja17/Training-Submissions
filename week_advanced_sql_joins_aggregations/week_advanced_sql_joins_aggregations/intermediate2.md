# Intermediate 2: Implementing Advanced Joins & Aggregations in Python (Pandas)

This task shows how to perform SQL-style joins and aggregations using Python Pandas.

---

## 🔹 Load the datasets
```python
import pandas as pd

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")
```

---

## 🔹 Step 1 — INNER JOIN: customers + orders
```python
df = custome

