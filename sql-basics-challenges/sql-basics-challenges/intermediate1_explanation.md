# Intermediate 1 — Explanation of Results

**Q1: Top customers by total spend**  
We aggregate `line_total` from the `v_order_details` view by `customer_id`. Sorting by the aggregated sum shows which customers spent the most overall. In this synthetic dataset, results may vary per random seed, but they illustrate the pattern.

**Q2: Monthly revenue trend**  
We bucket `order_date` to `YYYY-MM` and sum `line_total`. The output provides a time series of revenue useful for seasonality checks and planning. You can plot this to see an upward/downward trend or monthly swings.