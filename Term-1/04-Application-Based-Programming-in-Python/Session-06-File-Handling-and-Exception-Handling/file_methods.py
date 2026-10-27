# file_methods.py
# Useful file methods: tell, seek, readline, writelines, and the os module
import os

# writelines() writes a list of strings
cities = ["Karachi\n", "Lahore\n", "Quetta\n", "Peshawar\n"]
with open("cities.txt", "w", encoding="utf-8") as f:
    f.writelines(cities)

with open("cities.txt", "r", encoding="utf-8") as f:
    print("First line :", f.readline().strip())   # reads ONE line
    print("Position   :", f.tell())               # current position (in bytes)
    f.seek(0)                                     # jump back to the start
    print("Again      :", f.readline().strip())

# Checking and managing files with the os module
print("Exists?    :", os.path.exists("cities.txt"))
print("Size bytes :", os.path.getsize("cities.txt"))
os.rename("cities.txt", "pk_cities.txt")
print("Renamed    :", os.path.exists("pk_cities.txt"))
os.remove("pk_cities.txt")
print("Deleted    :", not os.path.exists("pk_cities.txt"))
