# NumPy Fundamentals — Challenge Set

This repository contains solutions for the full challenge set:
- **Easy 1:** Key concepts in your own words
- **Easy 2:** Toy example using NumPy
- **Intermediate 1:** Apply NumPy on a real dataset and explain results
- **Intermediate 2:** Implement NumPy fundamentals using an ML library
- **Hard 1:** Optimize the implementation for performance
- **Hard 2:** Mini project, end-to-end

## Quick Start
```bash
# (Optional) create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows PowerShell: .venv\Scripts\Activate.ps1

# Install minimal deps
pip install numpy scikit-learn matplotlib
# (Optional for extra speedups in Hard 1): pip install numba
```

## Run examples
```bash
# Easy 2
python easy2_toy_example.py

# Intermediate 1 (Iris dataset)
python intermediate1_real_dataset.py

# Intermediate 2 (scikit-learn + NumPy)
python intermediate2_sklearn_pipeline.py

# Hard 1 (vectorization & timing)
python hard1_optimization.py

# Hard 2 mini project (generate data then analyze)
python hard2_project/generate_data.py
python hard2_project/analysis.py
```
Artifacts:
- `hard2_project/data/sales_2024.csv` — synthetic dataset
- `hard2_project/figures/monthly_revenue.png` — saved plot

---

**Author:** Auto-generated on 2025-11-11 00:29:46
