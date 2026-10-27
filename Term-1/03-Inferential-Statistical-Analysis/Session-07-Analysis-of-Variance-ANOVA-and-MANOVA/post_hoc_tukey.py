# post_hoc_tukey.py
# After ANOVA says "some group is different", Tukey's HSD tells us WHICH ones.
import numpy as np
from scipy import stats

lecture = np.array([65, 70, 68, 72, 66, 69])
video   = np.array([70, 74, 73, 78, 71, 75])
project = np.array([78, 82, 80, 85, 79, 83])

# Step 1: run Tukey's honestly significant difference test
result = stats.tukey_hsd(lecture, video, project)

# Step 2: print each pair's p-value
names = ["lecture", "video", "project"]
for i in range(3):
    for j in range(i + 1, 3):
        p = result.pvalue[i, j]
        verdict = "different" if p < 0.05 else "similar"
        print(f"{names[i]:8} vs {names[j]:8}: p = {p:.4f} -> {verdict}")
