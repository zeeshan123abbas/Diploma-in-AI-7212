# hierarchical_clustering.py
# Agglomerative clustering: start with every point alone, then merge the closest pairs.

from sklearn.cluster import AgglomerativeClustering

# Marks of 8 students in [Maths, English]
marks = [[90, 85], [88, 80], [92, 88],   # strong in both
         [40, 90], [45, 85],             # strong in English only
         [85, 35], [80, 40], [83, 30]]   # strong in Maths only

model = AgglomerativeClustering(n_clusters=3, linkage="ward")
groups = model.fit_predict(marks)

for student, (row, group) in enumerate(zip(marks, groups), start=1):
    print(f"Student {student}: marks={row} -> group {group}")
