# task4_actual_vs_predicted.py  (Practice for Sessions 11 + 12)
# Task: visualise how good a degree-2 model is, using Seaborn.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("house_prices.csv")
df = df[df["area"] == "North Nazimabad"].copy()

poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(df[["size_sqft"]])
model = LinearRegression().fit(X_poly, df["price_lakh"])

df["predicted"] = model.predict(X_poly)
df["error"] = df["price_lakh"] - df["predicted"]     # residual = actual - predicted

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

# Left: actual vs predicted. Perfect predictions sit on the diagonal line.
sns.scatterplot(data=df, x="predicted", y="price_lakh", ax=axes[0])
low, high = df["price_lakh"].min(), df["price_lakh"].max()
axes[0].plot([low, high], [low, high], color="red", linestyle="--")
axes[0].set_title("Actual vs predicted price")

# Right: errors should be scattered randomly around zero
sns.histplot(data=df, x="error", kde=True, ax=axes[1])
axes[1].set_title("Prediction errors (residuals)")

fig.tight_layout()
fig.savefig("actual_vs_predicted.png")
print("Saved actual_vs_predicted.png")
print("Average absolute error:", round(df["error"].abs().mean(), 2), "lakh")
