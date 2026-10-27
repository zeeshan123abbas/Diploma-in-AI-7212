# spread_measures.py
# Measures of dispersion: how spread out is our data?
import numpy as np

# Step 1: daily sales (in Rs. thousands) of two shops for one week
shop_a = np.array([50, 52, 49, 51, 50, 48, 50])
shop_b = np.array([20, 80, 35, 70, 50, 30, 65])

for name, sales in [("Shop A", shop_a), ("Shop B", shop_b)]:
    # Step 2: range = biggest value minus smallest value
    data_range = sales.max() - sales.min()

    # Step 3: variance = average squared distance from the mean
    # ddof=1 means "sample" variance (divide by n - 1)
    variance = sales.var(ddof=1)

    # Step 4: standard deviation = square root of variance
    std_dev = sales.std(ddof=1)

    # Step 5: print a small report
    print(name)
    print("  mean     :", round(sales.mean(), 2))
    print("  range    :", data_range)
    print("  variance :", round(variance, 2))
    print("  std dev  :", round(std_dev, 2))

# Both shops have the same mean (50) but Shop B is far less predictable.
