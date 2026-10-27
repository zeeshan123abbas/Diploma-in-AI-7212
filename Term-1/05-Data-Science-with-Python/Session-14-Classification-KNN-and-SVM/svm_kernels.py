# svm_kernels.py
# When classes are NOT separable by a straight line, the kernel trick helps.

from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Two interleaving half-moons: impossible to split with one straight line
X, y = make_moons(n_samples=300, noise=0.2, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Try each kernel and compare test accuracy
for kernel in ["linear", "poly", "rbf"]:
    model = SVC(kernel=kernel, C=1.0)
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"Kernel {kernel:<6} accuracy = {acc:.3f}")

# The C parameter: small C = wider margin, allows some mistakes; big C = strict
print()
for c in [0.1, 1, 10, 100]:
    model = SVC(kernel="rbf", C=c).fit(X_train, y_train)
    print(f"RBF with C = {c:<5} accuracy = {accuracy_score(y_test, model.predict(X_test)):.3f}")
