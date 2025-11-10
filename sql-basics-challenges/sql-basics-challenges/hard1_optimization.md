# Hard 1 — Optimize for Performance

**Baseline:** Queries on `v_order_details` join four tables. On larger data, scans can be expensive.

**Indexes to add:**
```sql
CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id);
CREATE INDEX IF NOT EXISTS idx_order_items_order ON order_items(order_id);
CREATE INDEX IF NOT EXISTS idx_order_items_product ON order_items(product_id);
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);
CREATE INDEX IF NOT EXISTS idx_orders_date ON orders(order_date);
```
**Why:** These support common filters and joins: `orders.customer_id`, `order_items.order_id`, `order_items.product_id`, and date bucketing on `orders.order_date`.

**EXPLAIN (SQLite)**: After adding indexes, the planner can choose index scans instead of full table scans. For very large tables, this reduces I/O and speeds up joins/aggregations dramatically.

**Other tips:** Use `WHERE` clauses to reduce rows early; pre-aggregate with subqueries or CTEs; avoid `SELECT *` in large joins; cache dimension tables if your engine supports it.