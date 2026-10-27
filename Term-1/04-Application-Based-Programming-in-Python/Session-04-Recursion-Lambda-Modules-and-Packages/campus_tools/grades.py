# campus_tools/grades.py
# A module inside the campus_tools package

def calculate_grade(marks):
    """Convert marks (0-100) into a letter grade."""
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    return "F"
