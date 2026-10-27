# ml_workflow.py
# The complete Machine Learning workflow in small, clear steps.
# Dataset: the famous Iris flowers dataset that ships with scikit-learn.
# Command:  python ml_workflow.py

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1: Collect data
iris = load_iris()
X = iris.data        # features: sepal length, sepal width, petal length, petal width
y = iris.target      # label: 0 = setosa, 1 = versicolor, 2 = virginica
print("Step 1  rows:", X.shape[0], "| features:", X.shape[1])

# Step 2: Prepare data -> split into training part and testing part
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)   # 80% train, 20% test
print("Step 2  train rows:", len(X_train), "| test rows:", len(X_test))

# Step 3: Choose a model
model = KNeighborsClassifier(n_neighbors=3)  # looks at the 3 most similar flowers
print("Step 3  model:", model)

# Step 4: Train the model
model.fit(X_train, y_train)
print("Step 4  training finished")

# Step 5: Evaluate on data the model has never seen
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Step 5  accuracy on test data: {accuracy:.2%}")

# Step 6: Use the model on a brand new flower
new_flower = [[5.0, 3.4, 1.5, 0.2]]
predicted_class = model.predict(new_flower)[0]
print("Step 6  new flower is:", iris.target_names[predicted_class])
