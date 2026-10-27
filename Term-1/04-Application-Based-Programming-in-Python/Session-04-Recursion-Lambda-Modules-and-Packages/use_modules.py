# use_modules.py
# Different ways to import modules and packages

# 1) Import a built-in module
import math
print("sqrt(144) =", math.sqrt(144))

# 2) Import specific names from a module
from random import randint, seed
seed(5)
print("Random dice:", randint(1, 6))

# 3) Import with a short alias
import datetime as dt
print("Today:", dt.date.today())

# 4) Import our own module (my_math.py in the same folder)
import my_math
print("Area of circle r=3:", round(my_math.circle_area(3), 2))
print("Percentage:", my_math.percentage(42, 60))

# 5) Import from our own package (the campus_tools folder)
from campus_tools import calculate_grade, fee_after_discount
from campus_tools.grades import calculate_grade as grade_of
print("Grade for 74:", calculate_grade(74))
print("Grade for 85:", grade_of(85))
print("Fee after 20% discount:", fee_after_discount(30000, 20))

# 6) See what a module contains
print([name for name in dir(my_math) if not name.startswith("_")])
