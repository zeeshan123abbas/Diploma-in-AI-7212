# lambda_functions.py
# lambda = a small, one-line, unnamed function

# Step 1: a normal function and the same thing as a lambda
def double(x):
    return x * 2
double_lambda = lambda x: x * 2
print(double(5), double_lambda(5))

# Step 2: lambda with two parameters
add = lambda a, b: a + b
print("add:", add(3, 4))

# Step 3: sort a list of tuples by the second item (marks)
students = [("Ali", 72), ("Sara", 91), ("Bilal", 65)]
by_marks = sorted(students, key=lambda s: s[1], reverse=True)
print("Sorted by marks:", by_marks)

# Step 4: map() applies a function to every item
prices = [100, 250, 400]
with_tax = list(map(lambda p: round(p * 1.16, 2), prices))
print("With 16% tax:", with_tax)

# Step 5: filter() keeps items where the function returns True
marks = [45, 78, 90, 33, 61]
passed = list(filter(lambda m: m >= 50, marks))
print("Passed marks:", passed)
