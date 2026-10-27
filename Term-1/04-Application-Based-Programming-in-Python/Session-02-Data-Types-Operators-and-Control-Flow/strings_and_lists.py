# strings_and_lists.py
# Working with text and lists (the two types you will use most)

# ---- Strings ----
name = "Zeeshan Abbas"
print(name.upper())           # ZEESHAN ABBAS
print(name.lower())           # zeeshan abbas
print(len(name))              # number of characters
print(name[0])                # first character  -> Z
print(name[-1])               # last character   -> s
print(name[0:7])              # slicing          -> Zeeshan
print(name.split(" "))        # split into a list of words
print("Abbas" in name)        # membership test  -> True

# f-strings put variables inside text
age = 30
print(f"{name} is {age} years old.")

# ---- Lists ----
fruits = ["apple", "mango", "banana"]
fruits.append("orange")       # add at the end
fruits.insert(1, "grapes")    # add at position 1
fruits.remove("banana")       # remove by value
print(fruits)
print("Sorted:", sorted(fruits))
print("Count:", len(fruits))

# ---- Dictionaries ----
student = {"name": "Sara", "marks": 88}
student["city"] = "Lahore"    # add a new key
print(student["name"], student.get("city"))
for key, value in student.items():
    print(key, "=", value)
