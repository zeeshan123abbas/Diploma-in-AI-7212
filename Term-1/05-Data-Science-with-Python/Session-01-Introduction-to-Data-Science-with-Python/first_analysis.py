# first_analysis.py
# A tiny "data science" task with plain Python: answer questions from data.

# Monthly sales (in thousand rupees) of a small shop
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 128, 160, 172, 150]

# Question 1: What is the total and average sale?
total = sum(sales)
average = total / len(sales)
print("Total sales:", total)
print("Average sales:", round(average, 1))

# Question 2: Which month had the highest sale?
best_index = sales.index(max(sales))   # position of the biggest value
print("Best month:", months[best_index], "with", max(sales))

# Question 3: Which months were above average?
print("Months above average:")
for month, value in zip(months, sales):   # zip walks both lists together
    if value > average:
        print("  ", month, value)

# Question 4: Month-to-month growth in percent
print("Growth from previous month:")
for i in range(1, len(sales)):
    growth = (sales[i] - sales[i - 1]) / sales[i - 1] * 100
    print(f"   {months[i]}: {growth:+.1f}%")
