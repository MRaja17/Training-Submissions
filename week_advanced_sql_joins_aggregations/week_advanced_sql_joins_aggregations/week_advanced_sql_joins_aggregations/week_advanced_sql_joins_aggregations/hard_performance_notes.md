# Hard 1: SQL Performance Optimization Notes

This document summarizes important SQL optimization techniques used to improve query performance during joins and aggregations.

---

## ✔ 1. Use Indexes on Join Keys

Indexes help the database search faster.

**Example:**

```sql
CREATE INDEX idx_customer_id ON orders(customer_id);
