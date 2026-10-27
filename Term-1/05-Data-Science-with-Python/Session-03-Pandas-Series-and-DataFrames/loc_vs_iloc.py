# loc_vs_iloc.py
# loc  = select by LABEL (names)
# iloc = select by POSITION (numbers 0, 1, 2 ...)

import pandas as pd

df = pd.DataFrame(
    {"price": [250, 120, 900, 60], "stock": [10, 35, 4, 100]},
    index=["pen_box", "notebook", "bag", "eraser"],   # row labels
)
print(df, "\n")

# ---- loc: use row and column NAMES ----
print("loc['bag', 'price']        ->", df.loc["bag", "price"])
print("loc['notebook'] (full row) ->\n", df.loc["notebook"], "\n")
print("loc['pen_box':'bag', 'stock'] (end label INCLUDED) ->\n", df.loc["pen_box":"bag", "stock"], "\n")

# ---- iloc: use row and column POSITIONS ----
print("iloc[2, 0]          ->", df.iloc[2, 0])          # row 2, column 0 = bag price
print("iloc[0:2] (end position EXCLUDED) ->\n", df.iloc[0:2], "\n")
print("iloc[-1] (last row) ->\n", df.iloc[-1], "\n")

# ---- loc with a condition (very common) ----
print("Items with stock under 20 ->\n", df.loc[df["stock"] < 20], "\n")

# ---- change a value safely with loc ----
df.loc["bag", "stock"] = 15
print("After updating bag stock ->\n", df)
