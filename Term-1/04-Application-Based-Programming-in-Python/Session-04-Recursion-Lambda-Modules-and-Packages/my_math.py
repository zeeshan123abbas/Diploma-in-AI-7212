# my_math.py
# A MODULE is simply a .py file with functions and variables.
# Other files can import it.

PI = 3.14159

def circle_area(radius):
    """Return the area of a circle."""
    return PI * radius ** 2

def percentage(obtained, total):
    """Return obtained/total as a percentage."""
    return obtained / total * 100

# This block runs ONLY when you run my_math.py directly,
# not when another file imports it.
if __name__ == "__main__":
    print("Testing my_math:", circle_area(2), percentage(45, 50))
