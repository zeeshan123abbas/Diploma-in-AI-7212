# tk_calculator.py
# A simple application: add, subtract, multiply, divide two numbers
import tkinter as tk

window = tk.Tk()
window.title("Mini Calculator")
window.resizable(False, False)

# input boxes
first_entry = tk.Entry(window, width=12)
second_entry = tk.Entry(window, width=12)
first_entry.grid(row=0, column=0, padx=5, pady=5)
second_entry.grid(row=0, column=1, padx=5, pady=5)

# a label to show the result
result_label = tk.Label(window, text="Result: ", font=("Arial", 12, "bold"))
result_label.grid(row=2, column=0, columnspan=4, pady=10)

def calculate(operation):
    """Read both numbers, apply the operation, show the result."""
    try:
        a = float(first_entry.get())
        b = float(second_entry.get())
        if operation == "+":
            answer = a + b
        elif operation == "-":
            answer = a - b
        elif operation == "*":
            answer = a * b
        else:
            answer = a / b
        result_label.config(text=f"Result: {answer:g}", fg="black")
    except ValueError:
        result_label.config(text="Please enter numbers", fg="red")
    except ZeroDivisionError:
        result_label.config(text="Cannot divide by zero", fg="red")

# one button per operation; lambda passes the symbol to calculate()
for column, symbol in enumerate(["+", "-", "*", "/"]):
    tk.Button(window, text=symbol, width=5,
              command=lambda s=symbol: calculate(s)).grid(row=1, column=column, padx=2)

window.mainloop()
