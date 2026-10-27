# exceptions.py
# Handling errors so the program does not crash

# 1) try / except: catch a specific error
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# 2) Several except blocks + else + finally
def read_number(text):
    try:
        number = int(text)                 # may raise ValueError
    except ValueError:
        print(f"'{text}' is not a whole number")
    else:
        print("You entered", number)       # runs only if NO error
    finally:
        print("Check finished")            # ALWAYS runs

read_number("25")
read_number("abc")

# 3) Missing file
try:
    with open("does_not_exist.txt") as f:
        f.read()
except FileNotFoundError as error:
    print("File problem:", error)

# 4) raise your own error
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as error:
    print("Error caught:", error)

# 5) A custom exception class
class LowBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise LowBalanceError(f"Balance {balance} is less than {amount}")
    return balance - amount

try:
    withdraw(1000, 5000)
except LowBalanceError as error:
    print("Bank says:", error)
