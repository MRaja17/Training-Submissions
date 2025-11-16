# Hard 1: Performance Optimization for SQL Joins & Aggregations

Optimizing SQL queries is important for handling large datasets efficiently.  
Here are the best techniques used in real production systems:

---

# 🔹 1️⃣ Create Indexes for Faster Joins
Indexes make JOIN operations significantly faster.

```sql
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_product  ON orders(product_id);
```

---

# 🔹 2️⃣ Select Only the Required Columns
Avoid expensive operations like `SELECT *`.

❌ Bad:
```sql
SELECT *
FROM orders;
```

✅ Good:
```sql
SELECT order_id, customer_id, amount
FROM orders;
```

---

# 🔹 3️⃣ Pre-Aggregate Data Before Joining
You can summarize large tables first to reduce join cost.

```sql
SELECT 
    customer_id,
    SUM(amount) AS total_amount
INTO temp_order_totals
FROM orders
GROUP BY customer_id;
```

---

# 🔹 4️⃣ Replace Subqueries With Joins
JOINs are faster than correlated subqueries.

❌ Bad:
```sql
SELECT name,
       (SELECT SUM(amount) FROM orders WHERE id = customers.id)
FROM customers;
```

✅ Good:
```sql
SELECT c.name, SUM(o.amount)
FROM customers c
LEFT JOIN orders o ON c

