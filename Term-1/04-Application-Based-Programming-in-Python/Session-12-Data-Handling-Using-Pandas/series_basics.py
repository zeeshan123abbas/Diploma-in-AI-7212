# series_basics.py
# A Series is ONE column of data with labels (an index)
import pandas as pd

# Step 1: create a Series from a list (index 0, 1, 2 ... is added automatically)
marks = pd.Series([78, 91, 64, 85])
print(marks)

# Step 2: create a Series with our own labels
marks = pd.Series([78, 91, 64, 85], index=["Ali", "Sara", "Bilal", "Hina"], name="marks")
print("\nSara's marks:", marks["Sara"])

# Step 3: vectorised maths works on every value at once
print("\nWith 5 bonus marks:")
print(marks + 5)

# Step 4: filtering with a condition
print("\nAbove 80:")
print(marks[marks > 80])

# Step 5: quick statistics
print("\nMean:", marks.mean(), " Max:", marks.max(), " Top student:", marks.idxmax())

# Step 6: a Series from a dictionary
city_pop = pd.Series({"Karachi": 20.4, "Lahore": 13.0, "Faisalabad": 3.7})
print("\nPopulation (millions):")
print(city_pop.sort_values(ascending=False))
