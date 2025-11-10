# Easy 1 — Key Concepts of SQL Basics (in my own words)

**SQL (Structured Query Language)** is a language for interacting with relational databases. At a basic level, SQL helps you:
- **Create** tables and define their structure (`CREATE TABLE`).
- **Insert** data into tables (`INSERT`).
- **Read/query** data with flexible filters (`SELECT ... FROM ... WHERE ... ORDER BY ... LIMIT ...`).
- **Update** existing rows (`UPDATE`) and **delete** rows (`DELETE`).
- **Join** tables together using keys to answer real-world questions (`JOIN`).
- **Aggregate** and summarize data (`GROUP BY`, `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).

The heart of SQL Basics is thinking in **tables** (rows and columns), with **primary keys** that uniquely identify rows and **foreign keys** that connect tables. You write a **SELECT** statement that describes *what* results you want and let the database figure out *how* to retrieve them efficiently.