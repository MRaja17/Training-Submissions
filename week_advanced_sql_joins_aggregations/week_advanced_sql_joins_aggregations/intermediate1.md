# Intermediate 1: Real Dataset Analysis with Advanced Joins

## Objective
Analyze total revenue per customer by joining multiple tables.

## Example Tables
- `customers`
- `orders`
- `products`

---

# 🔹 Step 1 — Join customers and orders
```sql
SELECT *
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id;
```

---

# 🔹 Step 2 — Join with products to get price information
```sql
SELECT *
FROM orders o
JOIN products p
    ON o.product_id = p.product_id;
```

---

# 🔹 Step 3 — Final Query: Revenue Per Customer
```sql
SELECT 
    c.customer_id,
    c.customer_name,
    SUM(o.quantity * p.price) AS total_revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN products p
    ON o.product_id = p.product_id
GROUP BY 
    c.customer_id, c.customer_name
ORDER BY total_revenue DESC;
```

---

## 📌 Insights
- JOINs help combine information from multiple tables.
- Aggregations help calculate meaningful business metrics.
- This is how companies calculate revenue, customer spending, and performance KPIs.

