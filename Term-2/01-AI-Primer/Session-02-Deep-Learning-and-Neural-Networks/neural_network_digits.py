# neural_network_digits.py
# A small multi-layer neural network that reads handwritten digits (8x8 pixel images).
# Command:  python neural_network_digits.py

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# 1) Load 1,797 images of digits 0-9. Each image = 64 pixel values.
digits = load_digits()
X, y = digits.data, digits.target
print("Images:", X.shape[0], "| pixels per image:", X.shape[1])

# 2) Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

# 3) Scale pixels so every input has a similar range (helps the network learn)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4) Build the network: 64 inputs -> 32 neurons -> 16 neurons -> 10 outputs
network = MLPClassifier(hidden_layer_sizes=(32, 16), activation="relu",
                        max_iter=500, random_state=1)
network.fit(X_train, y_train)

# 5) Evaluate
predictions = network.predict(X_test)
print(f"Test accuracy: {accuracy_score(y_test, predictions):.2%}")
print("Layers (weight matrices):", [w.shape for w in network.coefs_])

# 6) Look at the first 10 test images
print("True     :", y_test[:10].tolist())
print("Predicted:", predictions[:10].tolist())
