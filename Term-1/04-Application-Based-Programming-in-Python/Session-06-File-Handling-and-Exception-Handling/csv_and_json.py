# csv_and_json.py
# Two file formats used everywhere in data science
import csv
import json

# ---- CSV: rows and columns, like Excel ----
students = [
    ["name", "city", "marks"],
    ["Ali", "Karachi", 78],
    ["Sara", "Lahore", 91],
    ["Bilal", "Multan", 64],
]
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)

with open("students.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)          # each row becomes a dictionary
    for row in reader:
        print(row["name"], "scored", row["marks"])

# ---- JSON: nested data, used by web APIs ----
profile = {"name": "Sara", "skills": ["Python", "SQL"], "active": True}
with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(profile, f, indent=2)

with open("profile.json", encoding="utf-8") as f:
    loaded = json.load(f)
print("Loaded skills:", loaded["skills"])
