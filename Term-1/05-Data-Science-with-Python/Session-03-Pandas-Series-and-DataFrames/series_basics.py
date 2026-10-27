# series_basics.py
# A pandas Series is a 1-D labelled column of data.

import pandas as pd   # "pd" is the usual short name

# 1) Series from a list (pandas adds labels 0, 1, 2 ... automatically)
marks = pd.Series([78, 85, 62, 90])
print(marks)

# 2) Series with our own labels (the index)
marks = pd.Series([78, 85, 62, 90], index=["Ali", "Hina", "Usman", "Zara"])
print("\nWith names as index:\n", marks)

# 3) Series from a dictionary: keys become the index
city_population = pd.Series({"Karachi": 20.4, "Lahore": 13.0, "Faisalabad": 3.6})
print("\nPopulation (millions):\n", city_population)

# 4) Reading values
print("\nHina's marks:", marks["Hina"])        # by label
print("First value:", marks.iloc[0])           # by position
print("Index:", list(marks.index))
print("Values:", marks.values)

# 5) Maths and statistics work on the whole Series
print("\nAdd 5 grace marks:\n", marks + 5)
print("Average:", marks.mean(), " Highest:", marks.max())
print("Who got the highest?", marks.idxmax())

# 6) Filtering
print("\nPassed with 70+:\n", marks[marks >= 70])
