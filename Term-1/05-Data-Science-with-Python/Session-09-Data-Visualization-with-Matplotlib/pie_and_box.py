# pie_and_box.py
# Pie chart = parts of a whole.  Box plot = median, spread and outliers.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ---- Pie chart: share of each payment method ----
methods = ["Cash on Delivery", "Card", "JazzCash", "EasyPaisa"]
share = [45, 25, 18, 12]

plt.figure(figsize=(5, 5))
plt.pie(share, labels=methods, autopct="%1.0f%%", startangle=90)   # autopct writes the %
plt.title("Payment Methods")
plt.tight_layout()
plt.savefig("pie_chart.png")

# ---- Box plot: delivery time (days) for three couriers ----
rng = np.random.default_rng(seed=5)
courier_a = rng.normal(3, 0.8, 40)
courier_b = rng.normal(4, 1.5, 40)
courier_c = np.append(rng.normal(2.5, 0.5, 38), [7, 8])   # two very late deliveries

plt.figure(figsize=(6, 4))
plt.boxplot([courier_a, courier_b, courier_c], tick_labels=["A", "B", "C"])
plt.title("Delivery Time by Courier")
plt.ylabel("Days")
plt.tight_layout()
plt.savefig("box_plot.png")
print("Saved pie_chart.png and box_plot.png")
