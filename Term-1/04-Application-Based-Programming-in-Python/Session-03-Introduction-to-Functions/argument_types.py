# argument_types.py
# Positional, keyword, default, *args and **kwargs

# 1) Positional arguments: matched by ORDER
def full_name(first, last):
    return first + " " + last
print(full_name("Ali", "Raza"))

# 2) Keyword arguments: matched by NAME (order does not matter)
print(full_name(last="Khan", first="Sana"))

# 3) Default arguments: used when no value is given
def fee_with_discount(fee, discount=10):
    return fee - fee * discount / 100
print(fee_with_discount(20000))        # uses 10%
print(fee_with_discount(20000, 25))    # uses 25%

# 4) *args: any number of positional values (arrive as a tuple)
def average(*numbers):
    return sum(numbers) / len(numbers)
print(average(70, 80, 90))
print(average(55, 65))

# 5) **kwargs: any number of keyword values (arrive as a dict)
def print_profile(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")
print_profile(name="Usman", city="Karachi", course="AI")
