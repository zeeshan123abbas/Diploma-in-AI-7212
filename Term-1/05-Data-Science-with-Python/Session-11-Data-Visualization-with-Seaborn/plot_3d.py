# plot_3d.py
# 3-D plots show THREE numeric variables at once (Matplotlib's 3-D toolkit).

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("students_performance.csv")

fig = plt.figure(figsize=(12, 5))

# 1) 3-D scatter: study hours, attendance and marks
ax1 = fig.add_subplot(1, 2, 1, projection="3d")          # projection="3d" makes a 3-D axes
colours = np.where(df["result"] == "Pass", "green", "red")
ax1.scatter(df["study_hours"], df["attendance"], df["marks"], c=colours, s=15)
ax1.set_xlabel("Study hours")
ax1.set_ylabel("Attendance")
ax1.set_zlabel("Marks")
ax1.set_title("3-D scatter (green = pass)")

# 2) 3-D surface: the "rule" marks = 10 + 6*hours + 0.35*attendance
hours = np.linspace(0.5, 7, 30)
attend = np.linspace(55, 100, 30)
H, A = np.meshgrid(hours, attend)          # every combination of hours and attendance
M = 10 + 6 * H + 0.35 * A
ax2 = fig.add_subplot(1, 2, 2, projection="3d")
ax2.plot_surface(H, A, M, cmap="viridis")
ax2.set_xlabel("Study hours")
ax2.set_ylabel("Attendance")
ax2.set_zlabel("Expected marks")
ax2.set_title("3-D surface")

fig.tight_layout()
fig.savefig("plot_3d.png")
print("Saved plot_3d.png")
