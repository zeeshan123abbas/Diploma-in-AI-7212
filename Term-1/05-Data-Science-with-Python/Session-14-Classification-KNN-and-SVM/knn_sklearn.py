# knn_sklearn.py
# KNN with scikit-learn on the famous Iris flower dataset (comes with sklearn).

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# 1) Load data: 150 flowers, 4 measurements, 3 species
iris = load_iris()
X, y = iris.data, iris.target
print("Features:", iris.feature_names)
print("Classes:", iris.target_names.tolist())

# 2) Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 3) Scale: learn mean/std from TRAIN only, apply to both
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4) Create and train the model (k = 5 neighbours)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# 5) Predict and measure accuracy
predictions = knn.predict(X_test_scaled)
print("\nAccuracy:", round(accuracy_score(y_test, predictions), 3))

# 6) Predict a brand-new flower
new_flower = [[5.9, 3.0, 5.1, 1.8]]   # sepal length, sepal width, petal length, petal width
species = knn.predict(scaler.transform(new_flower))[0]
print("New flower is:", iris.target_names[species])
