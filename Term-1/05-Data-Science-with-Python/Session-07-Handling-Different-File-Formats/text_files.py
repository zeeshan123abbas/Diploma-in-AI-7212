# text_files.py
# Reading and writing plain text (.txt) files.

# 1) WRITE: "w" creates the file (or replaces it). "with" closes it for us.
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Data science is fun.\n")
    file.write("Python makes it easy.\n")
    file.write("Practice every day.\n")
print("notes.txt written")

# 2) APPEND: "a" adds to the end without deleting old lines
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Clean data first!\n")

# 3) READ the whole file as one string
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("\nWhole file:\n" + content)

# 4) READ line by line (best for big files)
with open("notes.txt", "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(number, line.strip())    # strip() removes the "\n" at the end

# 5) A simple analysis: count words
words = content.split()
print("\nTotal words:", len(words))
