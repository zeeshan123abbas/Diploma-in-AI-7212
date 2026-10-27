# one_way_anova.py
# One-way ANOVA: do THREE or more groups have the same mean?
import numpy as np
from scipy import stats

# Step 1: marks of students taught by three different methods
lecture = np.array([65, 70, 68, 72, 66, 69])
video   = np.array([70, 74, 73, 78, 71, 75])
project = np.array([78, 82, 80, 85, 79, 83])

# Step 2: scipy does the whole test in one line
f_stat, p_value = stats.f_oneway(lecture, video, project)
print(f"F = {f_stat:.2f}, p = {p_value:.6f}")

# Step 3: the same F calculated by hand (to see the idea)
groups = [lecture, video, project]
all_marks = np.concatenate(groups)
grand_mean = all_marks.mean()

# between-group sum of squares: how far each group mean is from the grand mean
ss_between = sum(len(g) * (g.mean() - grand_mean) ** 2 for g in groups)
# within-group sum of squares: how far values are from their own group mean
ss_within = sum(((g - g.mean()) ** 2).sum() for g in groups)

k, n = len(groups), len(all_marks)
ms_between = ss_between / (k - 1)
ms_within = ss_within / (n - k)
print(f"Manual F = {ms_between / ms_within:.2f}")

# Step 4: decision
print("At least one method gives different marks" if p_value < 0.05 else "No difference between methods")
