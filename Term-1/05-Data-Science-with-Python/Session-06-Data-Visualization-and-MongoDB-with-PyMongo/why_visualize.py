# why_visualize.py
# The same numbers as a table and as a chart: which is easier to read?

import matplotlib
matplotlib.use("Agg")              # "Agg" = draw into files, no pop-up window
import matplotlib.pyplot as plt

cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]
orders = [520, 410, 260, 180, 90]

# 1) As text: you must read every number to compare
print("City       Orders")
for city, count in zip(cities, orders):
    print(f"{city:<10} {count}")

# 2) As a bar chart: the pattern is visible in one second
plt.figure(figsize=(7, 4))
plt.bar(cities, orders, color="steelblue")
plt.title("Online Orders by City")
plt.xlabel("City")
plt.ylabel("Number of orders")
plt.tight_layout()                 # avoids labels being cut off
plt.savefig("orders_by_city.png")  # saved in this folder
print("\nChart saved as orders_by_city.png")
