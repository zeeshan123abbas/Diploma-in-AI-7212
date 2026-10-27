# variables.py
# Creating variables and assigning values

# Step 1: a variable is a name that points to a value
student_name = "Ayesha"
age = 20
cgpa = 3.6
is_enrolled = True

# Step 2: print them, with their types
print(student_name, type(student_name))
print(age, type(age))
print(cgpa, type(cgpa))
print(is_enrolled, type(is_enrolled))

# Step 3: a variable can be given a new value (even a new type)
age = age + 1
print("Next year age:", age)

# Step 4: multiple assignment in one line
x, y, z = 10, 20, 30
print(x, y, z)

# Step 5: same value to many variables
p = q = r = 0
print(p, q, r)

# Step 6: swap two values the Python way
x, y = y, x
print("After swap:", x, y)

# Step 7: read input from the user (type your name when asked)
# name = input("Enter your name: ")
# print("Hello", name)
