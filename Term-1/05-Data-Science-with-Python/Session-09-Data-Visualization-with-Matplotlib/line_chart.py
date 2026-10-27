# line_chart.py
# Line chart = how something changes over time.

import matplotlib
matplotlib.use("Agg")                 # save to file instead of opening a window
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
karachi = [120, 135, 128, 160, 172, 150]
lahore = [100, 110, 125, 130, 128, 145]

plt.figure(figsize=(7, 4))                                   # width, height in inches
plt.plot(months, karachi, marker="o", label="Karachi")       # marker = dot on each point
plt.plot(months, lahore, marker="s", linestyle="--", label="Lahore")
plt.title("Monthly Sales (thousand Rs)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True, alpha=0.3)                                    # light background grid
plt.legend()                                                 # shows the labels box
plt.tight_layout()
plt.savefig("line_chart.png", dpi=100)
print("Saved line_chart.png")
