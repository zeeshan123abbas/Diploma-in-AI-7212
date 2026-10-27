# app_templates.py
# Using HTML templates (Jinja2) and a form that sends data with POST
from flask import Flask, render_template, request

app = Flask(__name__)

students = [
    {"name": "Ali", "marks": 78},
    {"name": "Sara", "marks": 91},
    {"name": "Bilal", "marks": 55},
]

@app.route("/")
def index():
    # pass Python data to the HTML template
    return render_template("index.html", title="Student List", students=students)

@app.route("/add", methods=["GET", "POST"])
def add_student():
    message = ""
    if request.method == "POST":
        # read values typed in the form
        name = request.form.get("name", "").strip()
        marks_text = request.form.get("marks", "0")
        if name and marks_text.isdigit():
            students.append({"name": name, "marks": int(marks_text)})
            message = f"{name} added successfully."
        else:
            message = "Please enter a name and whole-number marks."
    return render_template("add.html", title="Add Student", message=message)

if __name__ == "__main__":
    app.run(debug=True)
