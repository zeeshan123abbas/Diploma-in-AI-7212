# data_types.py
# The main built-in data types in Python

# Numbers
count = 25                 # int   (whole number)
price = 199.99             # float (decimal number)
z = 2 + 3j                 # complex (rarely used in data science)

# Text
course = "Python"          # str (string)

# Boolean
is_active = False          # bool: True or False

# Collections
marks = [70, 85, 90]                 # list  - ordered, changeable
point = (24.86, 67.01)               # tuple - ordered, NOT changeable
cities = {"Karachi", "Lahore"}       # set   - unique values, no order
student = {"name": "Ali", "age": 19} # dict  - key: value pairs

# Nothing
result = None              # NoneType: "no value yet"

# Print each value with its type
for value in [count, price, z, course, is_active, marks, point, cities, student, result]:
    print(type(value).__name__, "->", value)

# Type conversion (casting)
print(int("42") + 8)       # text to int -> 50
print(float(7))            # int to float -> 7.0
print(str(3.5) + " kg")    # number to text
print(list("abc"))         # string to list
