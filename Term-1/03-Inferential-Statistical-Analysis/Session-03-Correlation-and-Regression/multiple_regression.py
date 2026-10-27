# multiple_regression.py
# Multiple linear regression: predict house price from size AND rooms
import numpy as np
import pandas as pd

# Step 1: small housing table (price in Rs. lakh)
df = pd.DataFrame({
    "size_sq_yd": [120, 200, 240, 300, 400, 500],
    "rooms":      [2, 3, 3, 4, 5, 6],
    "price":      [82, 128, 152, 188, 255, 305],
})

# Step 2: build the X matrix with a column of 1s for the intercept
X = np.column_stack([np.ones(len(df)), df["size_sq_yd"], df["rooms"]])
y = df["price"].to_numpy()

# Step 3: solve least squares  (finds the best coefficients)
coef, *_ = np.linalg.lstsq(X, y, rcond=None)
intercept, b_size, b_rooms = coef
print("price =", round(intercept, 2), "+", round(b_size, 3), "* size +", round(b_rooms, 2), "* rooms")

# Step 4: predict a 350 sq yd, 4-room house
prediction = intercept + b_size * 350 + b_rooms * 4
print("Predicted price:", round(prediction, 1), "lakh")

# Step 5: correlation matrix shows how the columns relate
print(df.corr().round(3))
