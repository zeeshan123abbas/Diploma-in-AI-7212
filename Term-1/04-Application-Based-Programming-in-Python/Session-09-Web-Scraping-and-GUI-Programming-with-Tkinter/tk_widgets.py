# tk_widgets.py
# Common widgets and the grid() layout manager
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Student Registration")

# Labels and Entry boxes, placed with grid(row, column)
tk.Label(window, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
name_entry = tk.Entry(window, width=25)
name_entry.grid(row=0, column=1, padx=5)

# Radiobuttons share one variable
tk.Label(window, text="Batch:").grid(row=1, column=0, sticky="w", padx=5)
batch_var = tk.StringVar(value="Morning")
tk.Radiobutton(window, text="Morning", variable=batch_var, value="Morning").grid(row=1, column=1, sticky="w")
tk.Radiobutton(window, text="Evening", variable=batch_var, value="Evening").grid(row=2, column=1, sticky="w")

# Checkbutton: True/False
hostel_var = tk.BooleanVar()
tk.Checkbutton(window, text="Needs hostel", variable=hostel_var).grid(row=3, column=1, sticky="w")

# Listbox with choices
tk.Label(window, text="Course:").grid(row=4, column=0, sticky="nw", padx=5)
course_list = tk.Listbox(window, height=3)
for course in ["Python", "Statistics", "MongoDB"]:
    course_list.insert(tk.END, course)
course_list.grid(row=4, column=1, sticky="w")

def register():
    name = name_entry.get().strip()
    selected = course_list.curselection()
    if not name or not selected:
        messagebox.showwarning("Missing data", "Enter a name and select a course.")
        return
    course = course_list.get(selected[0])
    hostel = "Yes" if hostel_var.get() else "No"
    messagebox.showinfo("Registered", f"{name}\nBatch: {batch_var.get()}\nCourse: {course}\nHostel: {hostel}")

tk.Button(window, text="Register", command=register, bg="#0b5ed7", fg="white").grid(row=5, column=1, pady=10, sticky="w")

window.mainloop()
