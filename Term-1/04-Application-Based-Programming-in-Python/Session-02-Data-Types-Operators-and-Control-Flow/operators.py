# operators.py
# Arithmetic, comparison, logical, assignment, membership and identity operators
a, b = 17, 5

# Arithmetic
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)     # true division -> 3.4
print("a // b =", a // b)    # floor division -> 3
print("a % b  =", a % b)     # remainder -> 2
print("a ** 2 =", a ** 2)    # power -> 289

# Comparison (result is True/False)
print("a > b  :", a > b)
print("a == b :", a == b)
print("a != b :", a != b)

# Logical
age, has_cnic = 20, True
print("Can vote:", age >= 18 and has_cnic)
print("Weekend:", "Sat" == "Sun" or "Sun" == "Sun")
print("not True:", not True)

# Assignment shortcuts
total = 10
total += 5      # same as total = total + 5
total *= 2      # same as total = total * 2
print("total =", total)

# Membership and identity
print("m" in "mango")          # True
x = [1, 2]; y = x; w = [1, 2]
print(x is y, x is w, x == w)  # True False True

# Precedence: ** then * / // % then + -
print(2 + 3 * 4 ** 2)           # 2 + 3*16 = 50
