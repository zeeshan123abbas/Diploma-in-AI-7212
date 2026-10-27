# task2_polynomial_price.py  (Practice for Session 12)
# Task: predict price from size. Compare degree 1, 2 and 3 on test data.

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("house_prices.csv")
df = df[df["area"] == "North Nazimabad"]      # one area, so size is the main factor
X = df[["size_sqft"]]                          # double brackets -> 2-D table
y = df["price_lakh"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

best_degree, best_score = None, -999
for degree in [1, 2, 3]:
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    model = LinearRegression()
    model.fit(poly.fit_transform(X_train), y_train)
    score = r2_score(y_test, model.predict(poly.transform(X_test)))
    print(f"Degree {degree}: test R2 = {score:.3f}")
    # accept a more complex (higher degree) model only if it is clearly better
    if score > best_score + 0.005:
        best_degree, best_score = degree, score

print("\nBest degree:", best_degree)

# Refit the best model and predict a 2,500 sq ft house
poly = PolynomialFeatures(degree=best_degree, include_bias=False)
model = LinearRegression().fit(poly.fit_transform(X), y)
new_house = pd.DataFrame({"size_sqft": [2500]})
print("Predicted price for 2,500 sq ft:", round(model.predict(poly.transform(new_house))[0], 1), "lakh")
