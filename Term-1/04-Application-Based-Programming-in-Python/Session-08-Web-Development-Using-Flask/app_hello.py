# app_hello.py
# The smallest possible Flask web application.
# Run:  python app_hello.py   then open http://127.0.0.1:5000
from flask import Flask

# Step 1: create the application object
app = Flask(__name__)

# Step 2: a ROUTE connects a URL to a Python function (a "view")
@app.route("/")
def home():
    return "<h1>Hello from Flask!</h1><p>My first web page in Python.</p>"

# Step 3: start the development server
if __name__ == "__main__":
    app.run(debug=True)   # debug=True reloads on code changes (never in production)
