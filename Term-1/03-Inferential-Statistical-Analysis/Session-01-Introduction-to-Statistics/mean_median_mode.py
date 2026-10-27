# mean_median_mode.py
# Measures of central tendency: where is the "centre" of our data?
import statistics

# Step 1: marks of 10 students in a Python quiz (out of 20)
marks = [12, 15, 18, 15, 9, 20, 15, 11, 17, 14]

# Step 2: mean = add everything, divide by how many values
mean_value = statistics.mean(marks)

# Step 3: median = the middle value after sorting
median_value = statistics.median(marks)

# Step 4: mode = the value that appears most often
mode_value = statistics.mode(marks)

# Step 5: show the results
print("Sorted marks:", sorted(marks))
print("Mean  :", mean_value)
print("Median:", median_value)
print("Mode  :", mode_value)
