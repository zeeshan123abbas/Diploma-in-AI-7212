# define_and_call.py
# Creating (defining) and using (calling) functions

# A function with no parameters and no return value
def greet():
    """Print a welcome message."""
    print("Welcome to the Python class!")

# A function with a parameter
def greet_student(name):
    print(f"Hello, {name}!")

# A function that RETURNS a value
def square(number):
    return number * number

# A function that returns two values (as a tuple)
def min_and_max(values):
    return min(values), max(values)

# ---- calling the functions ----
greet()
greet_student("Hina")
result = square(9)
print("9 squared =", result)
low, high = min_and_max([45, 12, 89, 33])
print("Lowest:", low, "Highest:", high)

# Built-in functions are already defined for us
print(len("Python"), abs(-7), round(3.14159, 2), sum([1, 2, 3]))
help(greet)   # shows the docstring
