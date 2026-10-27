# tk_hello.py
# Your first Tkinter window: a label and a button.
import tkinter as tk

# Step 1: create the main window
window = tk.Tk()
window.title("My First GUI")
window.geometry("300x150")          # width x height in pixels

# Step 2: a function to run when the button is clicked
def say_hello():
    message_label.config(text="Hello, welcome to Tkinter!")

# Step 3: create widgets
message_label = tk.Label(window, text="Click the button", font=("Arial", 12))
hello_button = tk.Button(window, text="Say Hello", command=say_hello)

# Step 4: place widgets in the window
message_label.pack(pady=15)
hello_button.pack()

# Step 5: start the event loop (keeps the window open)
window.mainloop()
