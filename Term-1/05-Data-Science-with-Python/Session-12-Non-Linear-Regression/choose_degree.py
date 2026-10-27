# choose_degree.py
# How bendy should the curve be? Test different polynomial degrees on unseen data.

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# Make 60 noisy points that follow a gentle curve
rng = np.random.default_rng(seed=0)
x = rng.uniform(0, 10, 60)
y = 3 + 2 * x - 0.15 * x**2 + rng.normal(0, 1, 60)
X = x.reshape(-1, 1)

# Keep 30% of points aside to test the model on data it has never seen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

print("Degree   Train R2   Test R2")
for degree in [1, 2, 3, 4, 6]:
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    model = LinearRegression()
    model.fit(poly.fit_transform(X_train), y_train)
    train_r2 = r2_score(y_train, model.predict(poly.transform(X_train)))
    test_r2 = r2_score(y_test, model.predict(poly.transform(X_test)))
    print(f"{degree:>6}   {train_r2:8.3f}   {test_r2:7.3f}")

print("\nLook for the degree with the best TEST score, not the best train score.")
print("High train but lower test = overfitting (the curve memorised the noise).")
