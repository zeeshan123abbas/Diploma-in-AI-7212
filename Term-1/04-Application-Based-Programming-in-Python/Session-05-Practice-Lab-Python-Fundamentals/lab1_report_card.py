# lab1_report_card.py
# Practice: variables, data types, operators, if/elif/else, loops (Sessions 01-02)

# Step 1: store subject marks in a dictionary
student_name = "Hamza"
marks = {"Python": 84, "Statistics": 76, "SQL": 68, "MongoDB": 91, "English": 59}

# Step 2: calculate total, percentage and average with a loop
total = 0
for subject in marks:
    total += marks[subject]
percentage = total / (len(marks) * 100) * 100

# Step 3: decide the overall grade
if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "F"

# Step 4: print a neat report card using f-strings
print("=" * 30)
print(f"Report Card: {student_name}")
print("=" * 30)
for subject, score in marks.items():
    status = "Pass" if score >= 60 else "Fail"
    print(f"{subject:<12}{score:>5}   {status}")
print("-" * 30)
print(f"Total: {total}   Percentage: {percentage:.1f}%   Grade: {grade}")
