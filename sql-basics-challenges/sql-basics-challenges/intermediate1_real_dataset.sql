-- Intermediate 1 — Apply SQL Basics on a real dataset and explain results
-- Question 1: What are the top 5 customers by total spend?
SELECT
  customer_id,
  SUM(line_total) AS total_spend
FROM v_order_details
GROUP BY customer_id
ORDER BY total_spend DESC
LIMIT 5;

-- Question 2: Monthly revenue trend (YYYY-MM) with total revenue
SELECT
  strftime('%Y-%m', order_date) AS year_month,
  SUM(line_total) AS monthly_revenue
FROM v_order_details
GROUP BY year_month
ORDER BY year_month;