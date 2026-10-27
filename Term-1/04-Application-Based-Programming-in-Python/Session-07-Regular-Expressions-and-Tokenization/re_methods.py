# re_methods.py
# The most used functions of the re module
import re

sentence = "Python 3.12 was released in 2023 and Python 3.13 in 2024."

# re.search: first match anywhere (returns a Match object or None)
match = re.search(r"\d{4}", sentence)
print("search  :", match.group(), "at position", match.start())

# re.match: match only at the START of the string
print("match   :", re.match(r"Python", sentence) is not None)
print("match   :", re.match(r"released", sentence))      # None

# re.fullmatch: whole string must match (good for validation)
print("fullmatch:", bool(re.fullmatch(r"\d{5}-\d{7}-\d", "42101-1234567-1")))  # CNIC

# re.findall: list of all matches
print("findall :", re.findall(r"3\.\d+", sentence))

# re.finditer: loop over Match objects
for m in re.finditer(r"Python", sentence):
    print("finditer: found at", m.span())

# re.sub: replace matches
print("sub     :", re.sub(r"\d{4}", "YEAR", sentence))

# re.split: split on a pattern
print("split   :", re.split(r"[,;]\s*", "apple, mango;banana,  grapes"))

# groups ( ) capture parts of a match
email = "contact: zeeshan.abbas@example.com"
m = re.search(r"([\w.]+)@([\w.]+)", email)
print("user    :", m.group(1), "| domain:", m.group(2))

# compile a pattern once, use many times
phone_pattern = re.compile(r"^03\d{9}$")
for number in ["03001234567", "0300123", "04001234567"]:
    print(number, "valid?", bool(phone_pattern.match(number)))
