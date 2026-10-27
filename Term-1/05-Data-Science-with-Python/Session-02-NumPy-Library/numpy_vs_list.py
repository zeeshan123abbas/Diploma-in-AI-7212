# numpy_vs_list.py
# Why use a NumPy array instead of a normal Python list?

import time
import numpy as np

prices_list = [100, 250, 80]
prices_array = np.array([100, 250, 80])

# 1) Maths on every item
# With a list you need a loop:
with_tax_list = [p * 1.18 for p in prices_list]
print("List + 18% tax :", with_tax_list)
# With NumPy you write the maths once (this is called vectorisation):
print("Array + 18% tax:", prices_array * 1.18)

# 2) Be careful: "*" means different things!
print("\nList * 2 :", prices_list * 2)    # repeats the list
print("Array * 2:", prices_array * 2)     # doubles every value

# 3) Speed test on one million numbers
numbers_list = list(range(1_000_000))
numbers_array = np.arange(1_000_000)

start = time.time()
squares_list = [n * n for n in numbers_list]
list_time = time.time() - start

start = time.time()
squares_array = numbers_array * numbers_array
array_time = time.time() - start

print(f"\nList time : {list_time:.4f} seconds")
print(f"Array time: {array_time:.4f} seconds")
print("NumPy is roughly", round(list_time / max(array_time, 1e-6)), "times faster here")
