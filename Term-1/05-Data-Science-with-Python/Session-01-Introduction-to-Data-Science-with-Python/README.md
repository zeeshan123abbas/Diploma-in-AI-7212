# Session 01: Introduction to Data Science with Python

> Module: Data Science with Python · Diploma in AI · Term 1 · ⏱ ~2 hours

Every app you use (Daraz, Careem, YouTube, your bank) collects data and uses it to make decisions. **Data Science** is the skill of turning that raw data into answers. In this first session you will learn what kinds of data exist, why Python is the favourite language for this work, what a data scientist actually does all day, and you will run your first tiny analysis.

## 🎯 Learning Objectives

- Explain what data science is in simple words
- Identify structured, semi-structured and unstructured data, and numerical vs categorical values
- Explain why Python is widely used for data science
- Describe the role and daily workflow of a data scientist
- Give real-world use cases of data science in Pakistan and worldwide
- Check that Python and the core libraries are installed on your computer

## 📖 Concepts Explained

### 1. What is data science?

**Data science** combines three things: **programming** (to handle data), **statistics/maths** (to find patterns) and **domain knowledge** (to ask the right questions). The goal is always the same: *use data to make a better decision*.

> **Analogy:** A doctor looks at test reports (data), compares them with normal ranges (statistics) and uses medical knowledge (domain) to suggest a treatment (decision). A data scientist does the same for businesses.

### 2. Types of data

| Type | Meaning | Examples |
|---|---|---|
| **Structured** | Fixed rows and columns | Excel sheet, SQL table, attendance register |
| **Semi-structured** | Labelled fields but flexible shape | JSON from an API, MongoDB document, XML |
| **Unstructured** | No fixed format | WhatsApp messages, photos, voice notes, PDFs |

Inside a table, each column is also one of these kinds:

| Column kind | Sub-type | Example | What you can do |
|---|---|---|---|
| **Numerical** | Discrete (counts) | number of children | add, average |
| | Continuous (measured) | height 5.7 ft, price Rs 1,250.50 | add, average |
| **Categorical** | Nominal (no order) | city, gender, colour | count, group |
| | Ordinal (has order) | grade A/B/C, size S/M/L | count, sort |

> Tip: Ask yourself "does it make sense to take the average?" If yes, it is numerical. The average of city names makes no sense, so city is categorical.

### 3. Why Python for data science?

| Reason | What it means for you |
|---|---|
| Easy to read | Code looks almost like English, perfect for beginners |
| Huge library ecosystem | NumPy, pandas, Matplotlib, Seaborn, scikit-learn do the heavy lifting |
| Free and open source | No licence cost; runs on Windows, macOS and Linux |
| Notebooks | Jupyter and Google Colab let you mix code, charts and notes |
| Industry demand | Most data and AI job posts list Python as a must-have skill |

The libraries we will use in this module:

| Library | Job | Session |
|---|---|---|
| NumPy | fast arrays and maths | 02 |
| pandas | tables (DataFrames), cleaning, grouping | 03, 04, 08 |
| Matplotlib | basic charts | 09 |
| Seaborn | beautiful statistical charts | 11 |
| scikit-learn | machine learning models | 12, 14-17 |

### 4. The data science workflow

```mermaid
flowchart LR
  A[Ask a question] --> B[Collect data]
  B --> C[Clean data]
  C --> D[Explore and visualise]
  D --> E[Build a model]
  E --> F[Communicate results]
  F --> A
```

Most beginners expect to spend all day on fancy models. In reality, **collecting and cleaning data often takes 60-80% of the time**.

### 5. Why data scientists are important

A data scientist is a translator between data and decision makers. Typical duties:

- Talk to managers to understand the business problem
- Gather data from databases (SQL, MongoDB), files and APIs
- Clean messy data and handle missing values
- Create charts and dashboards that tell a clear story
- Build and test predictive models
- Explain results in simple language, not jargon

Related roles: **Data Analyst** (reports and dashboards), **Data Engineer** (pipelines and storage), **ML Engineer** (deploying models).

### 6. Real-world use cases

| Area | Use case |
|---|---|
| E-commerce | "Customers who bought this also bought..." recommendations |
| Banking | Detecting fraud on card transactions in real time |
| Ride-hailing | Predicting demand and surge pricing in each area of the city |
| Healthcare | Spotting disease early from X-rays and lab reports |
| Telecom | Predicting which customers may switch to another network (churn) |
| Agriculture | Forecasting crop yield from weather and soil data |
| Education | Finding students at risk of failing so teachers can help early |

### 7. Your tools

- **Anaconda**: installs Python plus most data libraries in one go.
- **Jupyter Notebook / JupyterLab**: run code cell by cell and see output right below.
- **Google Colab**: Jupyter in the browser, free, nothing to install.
- **VS Code**: a code editor; all `.py` files in this module run with `python file.py`.

## 💻 Code Examples

### Example 1: Check your setup

📄 File: [`check_setup.py`](./check_setup.py)

```python
# check_setup.py
# Run this first to confirm your computer is ready for the module.
# Command:  python check_setup.py

import sys  # sys tells us about the Python interpreter itself

print("Python version:", sys.version.split()[0])

# The list of libraries we will use in this module
libraries = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn"]

for name in libraries:
    try:
        module = __import__(name)            # try to import the library by its name
        version = getattr(module, "__version__", "unknown")
        print(f"OK      {name:<11} version {version}")
    except ImportError:
        print(f"MISSING {name:<11} -> install with: pip install {name if name != 'sklearn' else 'scikit-learn'}")
```

**How it works:** the loop tries to import each library. If the import works, it prints the version; if not, `ImportError` is caught and you see the exact `pip install` command to run.

### Example 2: Types of data in plain Python

📄 File: [`data_types.py`](./data_types.py)

```python
# data_types.py
# Shows the main TYPES OF DATA a data scientist meets, using plain Python.

# 1) Structured data: fixed columns, like a table or an Excel sheet
students = [
    {"name": "Ayesha", "age": 19, "city": "Karachi", "marks": 82},
    {"name": "Bilal",  "age": 21, "city": "Lahore",  "marks": 74},
    {"name": "Sara",   "age": 20, "city": "Karachi", "marks": 91},
]
print("Structured data (rows and columns):")
for row in students:
    print("  ", row)

# 2) Unstructured data: free text, images, audio (no fixed columns)
review = "The course was great but the lab PCs were slow."
print("\nUnstructured data (free text):")
print("  ", review)
print("   Number of words:", len(review.split()))

# 3) Semi-structured data: has labels (keys) but not a fixed table shape, e.g. JSON
tweet = {"user": "ali_99", "text": "Learning Python!", "tags": ["python", "ai"]}
print("\nSemi-structured data (JSON-like):")
print("  ", tweet)

# 4) Numerical vs categorical columns
ages = [row["age"] for row in students]      # numbers  -> we can do maths
cities = [row["city"] for row in students]   # labels   -> we count them
print("\nNumerical column 'age':", ages, "-> average =", sum(ages) / len(ages))
print("Categorical column 'city':", cities, "-> unique values =", set(cities))
```

**How it works:** a list of dictionaries behaves like a table (structured). A sentence is unstructured, so we can only do simple things like counting words. A dictionary holding a list inside is semi-structured. Finally we take the average of a numerical column and the unique values of a categorical column.

### Example 3: Your first mini analysis

📄 File: [`first_analysis.py`](./first_analysis.py)

```python
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
```

**How it works:** `sum()` and `len()` give the average, `max()` and `.index()` find the best month, `zip()` pairs each month with its sale, and a simple formula gives growth in percent. These are the same questions you will later answer in one line with pandas.

## 🧪 Lab Practice

1. Install Anaconda (or use Google Colab) and run `check_setup.py`. Install anything marked MISSING.
2. Open `data_types.py` and add two more students. Re-run and check the new average age.
3. In `first_analysis.py`, change the sales numbers to your own made-up values and find the worst month (hint: `min()`).
4. Make a table in your notebook with 10 columns from a form you filled recently (e.g. admission form) and label each column numerical/categorical and nominal/ordinal.
5. Search for one Pakistani company using data science and write 3 lines on what problem they solve.

## 📝 Assignment

Write `my_expenses.py` that stores your daily expenses for one week in a list, then prints: total, average, the most expensive day, and the days above average. Add a comment above every step.

## ❓ Quick Quiz

1. Is a JSON response from a weather API structured, semi-structured or unstructured?
2. "Shirt size: S, M, L, XL" is which kind of data?
3. Name the Python library used for tables in this module.
4. Which step of the data science workflow usually takes the most time?
5. Give one reason Python is popular for data science.

<details><summary>Answers</summary>

1. Semi-structured
2. Categorical, ordinal (it has a natural order)
3. pandas
4. Collecting and cleaning data
5. Any one: easy syntax, large libraries, free, notebooks, industry demand

</details>

## 💼 Interview Questions

1. **What is the difference between a data analyst and a data scientist?** An analyst mainly reports what happened using queries and dashboards; a data scientist also builds models that predict what will happen.
2. **What is the difference between structured and unstructured data?** Structured data fits fixed columns (tables); unstructured data like text, images and audio has no predefined format and needs extra processing.
3. **Walk me through a data science project lifecycle.** Define the question, collect data, clean it, explore and visualise, build and evaluate a model, then communicate and deploy the result.

## ✅ Summary

- Data science turns raw data into decisions using programming, statistics and domain knowledge.
- Data can be structured, semi-structured or unstructured; columns are numerical or categorical.
- Python wins because it is simple, free and has powerful libraries.
- The workflow is a loop: ask, collect, clean, explore, model, communicate.
- Use Anaconda, Jupyter, Colab or VS Code to run the examples.

---

[🏠 Module Home](../README.md) · [Next ➡](../Session-02-NumPy-Library/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
