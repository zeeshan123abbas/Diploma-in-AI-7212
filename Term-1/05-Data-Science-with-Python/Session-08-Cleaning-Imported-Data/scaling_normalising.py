# scaling_normalising.py
# Putting columns with very different ranges on the same scale.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.DataFrame({
    "age": [22, 35, 47, 29, 58],
    "income": [40000, 85000, 150000, 60000, 210000],
})
print("Original:\n", df, "\n")

# 1) Min-Max scaling by hand: (x - min) / (max - min) -> values between 0 and 1
manual = (df - df.min()) / (df.max() - df.min())
print("Min-Max (by hand):\n", manual.round(2), "\n")

# 2) The same with scikit-learn
minmax = MinMaxScaler()
scaled = minmax.fit_transform(df)                 # returns a NumPy array
print("Min-Max (sklearn):\n", pd.DataFrame(scaled, columns=df.columns).round(2), "\n")

# 3) Standardisation (z-score): (x - mean) / std -> mean 0, std 1
standard = StandardScaler()
z = standard.fit_transform(df)
z_df = pd.DataFrame(z, columns=df.columns).round(2)
print("Standardised:\n", z_df)
print("Mean of each column after:", z_df.mean().round(2).tolist())
