# app_routes.py
# Several routes, dynamic URL parts and returning JSON
from flask import Flask, jsonify

app = Flask(__name__)

courses = {"python": "Application Based Programming in Python",
           "stats": "Inferential Statistical Analysis"}

@app.route("/")
def home():
    return "Home page. Try /about, /hello/Ali, /square/7 or /api/courses"

@app.route("/about")
def about():
    return "This site is built with Flask."

# <name> is a variable part of the URL
@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name.title()}!"

# <int:number> only accepts whole numbers
@app.route("/square/<int:number>")
def square(number):
    return f"{number} squared is {number * number}"

# Return JSON data (how web APIs talk to apps)
@app.route("/api/courses")
def api_courses():
    return jsonify(courses)

if __name__ == "__main__":
    app.run(debug=True)
