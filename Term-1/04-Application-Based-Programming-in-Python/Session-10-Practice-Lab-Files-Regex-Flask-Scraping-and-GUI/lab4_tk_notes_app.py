# lab4_tk_notes_app.py
# Practice: Tkinter + file handling (Sessions 06 and 09)
# A tiny notes app that saves notes to notes.txt
import tkinter as tk
from tkinter import messagebox

NOTES_FILE = "notes.txt"

def load_notes():
    notes_list.delete(0, tk.END)
    try:
        with open(NOTES_FILE, encoding="utf-8") as f:
            for line in f:
                notes_list.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass                                   # no notes yet

def add_note():
    text = note_entry.get().strip()
    if not text:
        messagebox.showwarning("Empty", "Type a note first.")
        return
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    note_entry.delete(0, tk.END)
    load_notes()

window = tk.Tk()
window.title("Notes")

note_entry = tk.Entry(window, width=35)
note_entry.grid(row=0, column=0, padx=5, pady=5)
tk.Button(window, text="Add", command=add_note).grid(row=0, column=1, padx=5)
notes_list = tk.Listbox(window, width=45, height=8)
notes_list.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

load_notes()
window.mainloop()
