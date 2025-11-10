-- Easy 2 — Toy example applying SQL Basics
-- Goal: Find the top 5 most expensive products and list their name, category, and price.

-- You can run this in SQLite against data/data/sales.sqlite
SELECT product_name, category, price
FROM products
ORDER BY price DESC
LIMIT 5;