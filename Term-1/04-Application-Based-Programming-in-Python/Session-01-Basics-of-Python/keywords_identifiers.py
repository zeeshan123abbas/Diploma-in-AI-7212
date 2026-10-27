# keywords_identifiers.py
# Keywords are reserved words. Identifiers are names YOU choose.
import keyword

# Step 1: list all Python keywords (you cannot use these as names)
print("Number of keywords:", len(keyword.kwlist))
print(keyword.kwlist)

# Step 2: check if a word is a keyword
print("Is 'for' a keyword?  ", keyword.iskeyword("for"))
print("Is 'marks' a keyword?", keyword.iskeyword("marks"))

# Step 3: check if a name is a valid identifier
names = ["student_name", "_count", "2nd_place", "total-marks", "class", "Marks2"]
for name in names:
    valid = name.isidentifier() and not keyword.iskeyword(name)
    print(f"{name:13} -> valid identifier? {valid}")
