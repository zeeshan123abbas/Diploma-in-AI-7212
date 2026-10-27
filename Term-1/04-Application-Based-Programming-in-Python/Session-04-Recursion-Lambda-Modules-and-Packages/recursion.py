# recursion.py
# A recursive function is a function that calls ITSELF.

# Example 1: factorial  5! = 5 * 4 * 3 * 2 * 1
def factorial(n):
    if n <= 1:                 # base case: stops the recursion
        return 1
    return n * factorial(n - 1)   # recursive case: a smaller problem

print("5! =", factorial(5))

# Example 2: sum of digits  4729 -> 4 + 7 + 2 + 9 = 22
def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

print("Sum of digits of 4729 =", sum_of_digits(4729))

# Example 3: Fibonacci  0, 1, 1, 2, 3, 5, 8 ...
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("First 10 Fibonacci numbers:", [fibonacci(i) for i in range(10)])

# Example 4: countdown shows the order of calls
def countdown(n):
    if n == 0:
        print("Lift off!")
        return
    print(n)
    countdown(n - 1)

countdown(3)
