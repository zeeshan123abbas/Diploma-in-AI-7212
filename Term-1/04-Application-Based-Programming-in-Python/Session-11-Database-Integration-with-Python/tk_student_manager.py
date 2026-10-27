# tk_student_manager.py
# A Tkinter form to INSERT, UPDATE and DELETE student records in MySQL.
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from db_config import DB_CONFIG

def run_sql(sql, values=()):
    """Run an INSERT/UPDATE/DELETE and return the affected row count."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()
    count = cursor.rowcount
    conn.close()
    return count

def fetch_all():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, city, marks FROM students ORDER BY id")
    rows = cursor.fetchall()
    conn.close()
    return rows

def refresh_list():
    records.delete(0, tk.END)
    for row in fetch_all():
        records.insert(tk.END, f"{row[0]:>3} | {row[1]:<12} | {row[2]:<10} | {row[3]}")

def read_form():
    return id_entry.get().strip(), name_entry.get().strip(), city_entry.get().strip(), marks_entry.get().strip()

def insert_record():
    _, name, city, marks = read_form()
    if not name or not marks.isdigit():
        messagebox.showwarning("Check input", "Name and numeric marks are required.")
        return
    run_sql("INSERT INTO students (name, city, marks) VALUES (%s, %s, %s)", (name, city, int(marks)))
    refresh_list()

def update_record():
    sid, name, city, marks = read_form()
    if not sid.isdigit() or not marks.isdigit():
        messagebox.showwarning("Check input", "Enter the ID and numeric marks.")
        return
    count = run_sql("UPDATE students SET name=%s, city=%s, marks=%s WHERE id=%s", (name, city, int(marks), int(sid)))
    messagebox.showinfo("Update", f"{count} record(s) updated")
    refresh_list()

def delete_record():
    sid = id_entry.get().strip()
    if sid.isdigit() and messagebox.askyesno("Confirm", f"Delete student {sid}?"):
        run_sql("DELETE FROM students WHERE id=%s", (int(sid),))
        refresh_list()

window = tk.Tk()
window.title("Student Manager (MySQL)")

labels = ["ID (for update/delete)", "Name", "City", "Marks"]
entries = []
for row, text in enumerate(labels):
    tk.Label(window, text=text).grid(row=row, column=0, sticky="w", padx=5, pady=2)
    entry = tk.Entry(window, width=25)
    entry.grid(row=row, column=1, padx=5, pady=2)
    entries.append(entry)
id_entry, name_entry, city_entry, marks_entry = entries

buttons = tk.Frame(window)
buttons.grid(row=4, column=0, columnspan=2, pady=8)
tk.Button(buttons, text="Insert", width=8, command=insert_record).pack(side="left", padx=3)
tk.Button(buttons, text="Update", width=8, command=update_record).pack(side="left", padx=3)
tk.Button(buttons, text="Delete", width=8, command=delete_record).pack(side="left", padx=3)

records = tk.Listbox(window, width=50, font=("Courier New", 10))
records.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

try:
    refresh_list()
except mysql.connector.Error as error:
    messagebox.showerror("Database", f"Cannot connect: {error}")

window.mainloop()
