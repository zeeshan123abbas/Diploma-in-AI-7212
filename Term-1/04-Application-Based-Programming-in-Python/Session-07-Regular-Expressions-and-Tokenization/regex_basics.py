# regex_basics.py
# Character classes, special sequences and metacharacters
import re

text = "Order #4521 placed on 2026-10-27 by Ali. Call 0300-1234567. Total Rs. 3,450"

# \d = any digit, + = one or more
print("All numbers     :", re.findall(r"\d+", text))

# [A-Z] = character class: any capital letter, \w = letter/digit/underscore
print("Capital words   :", re.findall(r"[A-Z]\w*", text))

# {n} = exactly n times -> a date pattern YYYY-MM-DD
print("Date            :", re.findall(r"\d{4}-\d{2}-\d{2}", text))

# A Pakistani mobile number pattern 03XX-XXXXXXX
print("Mobile          :", re.findall(r"03\d{2}-\d{7}", text))

# ^ = start of string, $ = end of string
print("Starts 'Order'? :", bool(re.search(r"^Order", text)))
print("Ends with digit?:", bool(re.search(r"\d$", text)))

# . = any character, \. = a real dot, ? = optional
print("Rs amounts      :", re.findall(r"Rs\.?\s?[\d,]+", text))

# | = OR
print("Ali or Sara     :", re.findall(r"Ali|Sara", text))
