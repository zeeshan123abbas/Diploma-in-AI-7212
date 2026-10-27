# write_and_read.py
# Writing a text file, appending to it, and reading it back

# Step 1: write mode "w" creates the file (or empties it if it exists)
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python file handling\n")
    file.write("Line 2: writing text\n")

# Step 2: append mode "a" adds to the end without deleting old content
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Line 3: appended later\n")

# Step 3: read the whole file as one string
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("--- read() ---")
print(content)

# Step 4: read line by line (memory friendly for big files)
print("--- line by line ---")
with open("notes.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(line_number, line.strip())

# Step 5: readlines() gives a list of lines
with open("notes.txt", encoding="utf-8") as file:
    lines = file.readlines()
print("Number of lines:", len(lines))
