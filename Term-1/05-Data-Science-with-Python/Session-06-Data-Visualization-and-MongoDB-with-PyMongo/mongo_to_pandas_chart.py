# mongo_to_pandas_chart.py
# Typical data science flow: MongoDB -> pandas DataFrame -> chart (PNG file).
# Run mongo_insert_find.py first so the collection has data.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=3000)
students = client["aptech_ds"]["students"]

# 1) Read the documents (hide the _id field) into a list of dictionaries
documents = list(students.find({}, {"_id": 0}))

# 2) Turn the list into a DataFrame
df = pd.DataFrame(documents)
print(df)

# 3) Average marks per city with pandas
city_avg = df.groupby("city")["marks"].mean()
print("\nAverage marks per city:\n", city_avg)

# 4) Draw and save a bar chart
plt.figure(figsize=(6, 4))
plt.bar(city_avg.index, city_avg.values, color="seagreen")
plt.title("Average Marks by City (from MongoDB)")
plt.ylabel("Average marks")
plt.tight_layout()
plt.savefig("mongo_city_marks.png")
print("\nChart saved as mongo_city_marks.png")

client.close()
