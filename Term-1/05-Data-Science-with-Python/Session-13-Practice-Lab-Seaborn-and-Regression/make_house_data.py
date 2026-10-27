# make_house_data.py
# Creates house_prices.csv (150 houses) for this lab.

import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=13)
n = 150
size = rng.uniform(500, 4000, n).round()                     # square feet
area = rng.choice(["Gulshan", "DHA", "North Nazimabad", "Malir"], n)
age = rng.integers(0, 30, n)
area_factor = pd.Series(area).map({"DHA": 1.5, "Gulshan": 1.1, "North Nazimabad": 1.0, "Malir": 0.7}).values

# price grows faster than size (a curve) and drops a little with age
price = (20 + 0.000012 * size**2 + 0.01 * size) * area_factor - age * 0.6 + rng.normal(0, 8, n)
df = pd.DataFrame({"size_sqft": size, "area": area, "age_years": age, "price_lakh": price.round(1)})
df.to_csv("house_prices.csv", index=False)
print("Created house_prices.csv with", len(df), "rows")
