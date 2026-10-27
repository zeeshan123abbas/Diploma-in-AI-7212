# lab2_notes_api.py
# Practice: Flask + JSON file storage (Sessions 06 and 08)
# Run: python lab2_notes_api.py   then open http://127.0.0.1:5000/notes
import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)
DATA_FILE = "notes.json"

def load_notes():
    """Read notes from the JSON file (empty list if file is missing)."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)

@app.route("/notes", methods=["GET"])
def list_notes():
    return jsonify(load_notes())

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json(silent=True) or {}
    text = str(data.get("text", "")).strip()
    if not text:
        return jsonify({"error": "text is required"}), 400   # 400 = bad request
    notes = load_notes()
    note = {"id": len(notes) + 1, "text": text}
    notes.append(note)
    save_notes(notes)
    return jsonify(note), 201                               # 201 = created

if __name__ == "__main__":
    app.run(debug=True)
