# first_ml_model.py
# The full ML workflow in a few lines: load -> split -> train -> predict -> evaluate.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1) Load a small built-in dataset (150 flowers, 4 measurements each)
iris = load_iris()
X = iris.data      # features (inputs)
y = iris.target    # labels (answers: 0, 1 or 2)
print("Data shape:", X.shape)

# 2) Keep 30% of the data aside to test the model fairly
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 3) Create and train the model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# 4) Predict on data the model has never seen
predictions = model.predict(X_test)

# 5) Evaluate: how many predictions were correct?
accuracy = accuracy_score(y_test, predictions)
print("Accuracy on test data:", round(accuracy * 100, 1), "%")

# 6) Use the model for one new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]
label = model.predict(new_flower)[0]
print("New flower is:", iris.target_names[label])
