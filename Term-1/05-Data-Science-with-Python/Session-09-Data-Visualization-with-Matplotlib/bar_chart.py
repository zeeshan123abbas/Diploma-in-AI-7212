# bar_chart.py
# Bar chart = compare amounts between categories.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

courses = ["Python", "SQL", "MongoDB", "Statistics"]
students = [45, 38, 30, 25]

# 1) Vertical bars
plt.figure(figsize=(6, 4))
bars = plt.bar(courses, students, color=["#4C72B0", "#55A868", "#C44E52", "#8172B2"])
plt.bar_label(bars)                     # write the value on top of each bar
plt.title("Enrolled Students per Course")
plt.ylabel("Students")
plt.tight_layout()
plt.savefig("bar_chart.png")

# 2) Horizontal bars are easier to read when labels are long
plt.figure(figsize=(6, 4))
plt.barh(courses, students, color="teal")
plt.title("Enrolled Students (horizontal)")
plt.xlabel("Students")
plt.tight_layout()
plt.savefig("barh_chart.png")
print("Saved bar_chart.png and barh_chart.png")
