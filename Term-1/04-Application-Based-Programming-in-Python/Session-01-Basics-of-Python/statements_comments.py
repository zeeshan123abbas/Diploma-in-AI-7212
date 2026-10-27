# statements_comments.py
# Statements, comments, indentation and line continuation

# This is a single-line comment. Python ignores it.

"""
This is a docstring / multi-line string.
It is often used to describe a file or a function.
"""

# One statement per line (the normal style)
city = "Karachi"
print(city)

# Several statements on one line using ; (allowed, but avoid it)
a = 1; b = 2; print(a + b)

# A long statement split over lines with brackets (implicit continuation)
total = (10 + 20 +
         30 + 40)
print("Total:", total)

# Indentation (4 spaces) marks a block of code
marks = 75
if marks >= 50:
    print("Pass")          # inside the if-block
    print("Well done!")    # also inside
print("This line always runs")  # outside the block
