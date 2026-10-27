# json_files.py
# JSON = the format used by web APIs and MongoDB. Python handles it with the json module.

import json
import pandas as pd

# 1) A Python dictionary with a nested list
course = {
    "course": "Data Science with Python",
    "sessions": 18,
    "students": [
        {"name": "Asad", "marks": 81},
        {"name": "Mehwish", "marks": 92},
    ],
}

# 2) WRITE to a .json file (indent=2 makes it nicely readable)
with open("course.json", "w", encoding="utf-8") as file:
    json.dump(course, file, indent=2)
print("course.json written")

# 3) READ it back into a dictionary
with open("course.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)
print("Course name:", loaded["course"])
print("First student:", loaded["students"][0]["name"])

# 4) Convert between a JSON string and Python
text = json.dumps({"city": "Karachi", "temp": 34})   # dict -> string
print("\nAs a string:", text)
back = json.loads(text)                               # string -> dict
print("Back to dict, temp =", back["temp"])

# 5) Nested JSON straight into a table with pandas
table = pd.json_normalize(loaded, record_path="students", meta=["course"])
print("\nAs a DataFrame:\n", table)
