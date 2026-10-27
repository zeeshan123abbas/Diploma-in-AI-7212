# data_types.py
# Shows the main TYPES OF DATA a data scientist meets, using plain Python.

# 1) Structured data: fixed columns, like a table or an Excel sheet
students = [
    {"name": "Ayesha", "age": 19, "city": "Karachi", "marks": 82},
    {"name": "Bilal",  "age": 21, "city": "Lahore",  "marks": 74},
    {"name": "Sara",   "age": 20, "city": "Karachi", "marks": 91},
]
print("Structured data (rows and columns):")
for row in students:
    print("  ", row)

# 2) Unstructured data: free text, images, audio (no fixed columns)
review = "The course was great but the lab PCs were slow."
print("\nUnstructured data (free text):")
print("  ", review)
print("   Number of words:", len(review.split()))

# 3) Semi-structured data: has labels (keys) but not a fixed table shape, e.g. JSON
tweet = {"user": "ali_99", "text": "Learning Python!", "tags": ["python", "ai"]}
print("\nSemi-structured data (JSON-like):")
print("  ", tweet)

# 4) Numerical vs categorical columns
ages = [row["age"] for row in students]      # numbers  -> we can do maths
cities = [row["city"] for row in students]   # labels   -> we count them
print("\nNumerical column 'age':", ages, "-> average =", sum(ages) / len(ages))
print("Categorical column 'city':", cities, "-> unique values =", set(cities))
