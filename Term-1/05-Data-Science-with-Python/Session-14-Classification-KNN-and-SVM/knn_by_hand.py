# knn_by_hand.py
# K-Nearest Neighbours explained with plain Python: "tell me who your neighbours are".

import math

# Known fruits: (weight in grams, sweetness 1-10) -> label
known = [
    (150, 7, "Apple"), (170, 8, "Apple"), (140, 6, "Apple"),
    (120, 9, "Mango"), (200, 9, "Mango"), (220, 10, "Mango"),
    (80, 3, "Lemon"), (90, 2, "Lemon"), (70, 3, "Lemon"),
]
new_fruit = (160, 8)    # we don't know what this is
k = 3

# Step 1: distance from the new fruit to every known fruit (straight-line distance)
distances = []
for weight, sweet, label in known:
    d = math.sqrt((weight - new_fruit[0]) ** 2 + (sweet - new_fruit[1]) ** 2)
    distances.append((d, label))

# Step 2: sort by distance and keep the k closest
distances.sort()
nearest = distances[:k]
print("The", k, "nearest neighbours:")
for d, label in nearest:
    print(f"   {label:<6} distance {d:.1f}")

# Step 3: majority vote
votes = {}
for d, label in nearest:
    votes[label] = votes.get(label, 0) + 1
prediction = max(votes, key=votes.get)
print("Votes:", votes, "-> prediction:", prediction)
# Note: weight (grams) has a much bigger range than sweetness, so it dominates the distance.
# That is why we SCALE features before KNN (see knn_sklearn.py).
