# make_sales_csv.py
# Creates the practice file "sales.csv" used in this session.
# Run it once:  python make_sales_csv.py

import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=7)      # fixed seed -> same data every time
rows = 60

data = pd.DataFrame({
    "order_id": range(1001, 1001 + rows),
    "date": pd.date_range("2026-01-01", periods=rows, freq="3D").strftime("%Y-%m-%d"),
    "city": rng.choice(["Karachi", "Lahore", "Islamabad", "Peshawar"], size=rows),
    "category": rng.choice(["Electronics", "Clothing", "Grocery"], size=rows),
    "quantity": rng.integers(1, 10, size=rows),
    "unit_price": rng.choice([250, 800, 1500, 3200, 12000], size=rows),
})

data.to_csv("sales.csv", index=False)    # index=False -> don't write row numbers
print("sales.csv created with", len(data), "rows")
