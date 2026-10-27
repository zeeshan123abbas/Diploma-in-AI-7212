# lab2_number_tools.py
# Practice: functions, return values, recursion (Sessions 03-04)

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True

def gcd(a, b):
    """Greatest common divisor using recursion (Euclid's method)."""
    if b == 0:
        return a
    return gcd(b, a % b)

def reverse_number(n):
    """Reverse the digits: 1234 -> 4321 (uses a while loop)."""
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return reversed_n

def is_palindrome(n):
    return n == reverse_number(n)

# ---- test the functions ----
print("Primes up to 30:", [n for n in range(31) if is_prime(n)])
print("gcd(48, 18) =", gcd(48, 18))
print("reverse(1234) =", reverse_number(1234))
for n in [121, 123, 4554]:
    print(n, "palindrome?", is_palindrome(n))
