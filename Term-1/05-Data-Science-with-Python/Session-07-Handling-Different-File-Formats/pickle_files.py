# pickle_files.py
# Pickle saves ANY Python object to a file and loads it back exactly the same.
# Warning: only load pickle files you created yourself (they can run code).

import pickle
import pandas as pd

# 1) Save a normal Python object (a dictionary with a list inside)
settings = {"model": "KNN", "k": 5, "features": ["age", "income"]}
with open("settings.pkl", "wb") as file:      # "wb" = write binary
    pickle.dump(settings, file)
print("settings.pkl saved")

# 2) Load it back
with open("settings.pkl", "rb") as file:      # "rb" = read binary
    loaded = pickle.load(file)
print("Loaded:", loaded, "| same as before?", loaded == settings)

# 3) pandas has shortcut methods for DataFrames
df = pd.DataFrame({"product": ["Pen", "Book"], "price": [50, 400]})
df.to_pickle("products.pkl")
df_back = pd.read_pickle("products.pkl")
print("\nDataFrame from pickle:\n", df_back)
print("Column types kept:", dict(df_back.dtypes.astype(str)))
