-- Easy 2: Toy Example for Advanced SQL Joins & Aggregations

-- Create tables
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(10,2)
);

-- Insert sample data
INSERT INTO customers (customer_id, customer_name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

INSERT INTO orders (order_id, customer_id, amount) VALUES
(101, 1, 50.00),
(102, 1, 30.00),
(103, 2, 20.00);

-- Example 1: INNER JOIN
SELECT
    c.customer_name,
    o.order_id,
    o.amount
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id;

-- Example 2: LEFT JOIN
SELECT
    c.customer_name,
    o.order_id,
    o.amount
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id;

-- Example 3: Aggregation (Total spent per customer)
SELECT
    c.customer_name,
    SUM(o.amount) AS total_spent
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name;

-- Example 4: HAVING clause (Customers who spent > 40)
SELECT
    c.customer_name,
    SUM(o.amount) AS total_spent
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name
HAVING SUM(o.amount) > 40;
