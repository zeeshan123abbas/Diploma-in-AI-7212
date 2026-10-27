# make_students_data.py
# Creates students_performance.csv (200 students) used by all examples in this session.

import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=11)
n = 200

study_hours = rng.uniform(0.5, 7, n).round(1)
attendance = rng.integers(55, 100, n)
gender = rng.choice(["Male", "Female"], n)
section = rng.choice(["A", "B", "C"], n)
internet = rng.choice(["Yes", "No"], n, p=[0.7, 0.3])

# marks depend on study hours and attendance, plus some random noise
marks = 10 + study_hours * 6 + attendance * 0.35 + rng.normal(0, 6, n)
marks = np.clip(marks, 0, 100).round()

df = pd.DataFrame({
    "gender": gender, "section": section, "internet": internet,
    "study_hours": study_hours, "attendance": attendance, "marks": marks,
})
df["result"] = np.where(df["marks"] >= 50, "Pass", "Fail")
df.to_csv("students_performance.csv", index=False)
print("Created students_performance.csv with", len(df), "rows")
print(df.head())
