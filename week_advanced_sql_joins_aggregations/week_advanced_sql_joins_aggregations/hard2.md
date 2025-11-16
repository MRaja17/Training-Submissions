# Hard 2: End-to-End Mini Project Using SQL Joins & Aggregations

This project demonstrates how SQL powers a full analytics pipeline  
to compute **Customer Lifetime Value (CLV)** using multiple joins and aggregations.

---

# 🎯 Project Goal
Calculate lifetime revenue for each customer using:
- customer data  
- orders  
- products  
- transactions  

---

# 🔹 Step 1 — Understand the Tables

### customers
| customer_id | customer_name |

### orders
| order_id | customer_id | product_id | quantity |

### products
| product_id | price |

### transactions
| transaction_id | order_id | timestamp |

---

# 🔹 Step 2 — Perform Full Join Analysis

```sql
SELECT 
    c.customer_id,
    c.customer_name,
    SUM(o.quantity * p.price) AS lifetime_value
FROM customers c
JOIN orders o 
    ON c.customer_id = o.customer_id
JOIN products p 
    ON o.product_id = p.product_id
GROUP BY 
    c.customer_id, c.customer_name
ORDER BY 
    lifetime_value DESC;
```

---

# 🔹 Step 3 — Export Results

```sql
COPY (
    SELECT 
        c.customer_id,
        c.customer_name,
        SUM(o.quantity * p.price) AS lifetime_value
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN products p ON o.product_id = p.product_id
    GROUP BY c.customer_id, c.customer_name
) TO '/output/customer_ltv.csv' CSV HEADER;
```

---

# 🔹 Step 4 — Insights and Interpretation

- Customers with many orders show higher CLV.
- Expensive products increase total revenue impact.
- Helps with business decisions such as:
  - marketing investment  
  - retention plans  
  - personalized offers  

---

# ✅ **Project Completed**
This end-to-end project correctly applies:
- Multi-table JOINs  
- Aggregations  
- Business analytics logic  
- Exporting datasets  

A complete SQL-based mini project!

