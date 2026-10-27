# control_flow.py
# Decisions (if/elif/else, match) and loops (for, while)

# ---- if / elif / else: convert marks to a grade ----
marks = 78
if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"
print("Grade:", grade)

# ---- match (Python 3.10+): a cleaner way to compare one value ----
day = "Sat"
match day:
    case "Sat" | "Sun":
        print("Weekend")
    case _:
        print("Weekday")

# ---- for loop: repeat for each item ----
for number in range(1, 6):       # 1, 2, 3, 4, 5
    print(number, "x 7 =", number * 7)

# ---- while loop: repeat while a condition is True ----
balance = 1000
months = 0
while balance < 1500:
    balance = balance * 1.10     # 10% growth per month
    months += 1
print("Months to reach 1500:", months)

# ---- break and continue ----
for n in range(1, 11):
    if n % 2 == 0:
        continue                 # skip even numbers
    if n > 7:
        break                    # stop the loop completely
    print("odd:", n)
