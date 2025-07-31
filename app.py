from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data.json"

KEYWORDS_TO_TAGS = {
    "project": "Work",
    "deadline": "Urgent",
    "idea": "Idea",
    "task": "To-Do",
    "meeting": "Work",
    "read": "Personal",
    "urgent": "Urgent",
    "learn": "Personal Growth",
    "buy": "Shopping",
    "call": "Reminder"
}

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def auto_tag(text):
    tags = set()
    for keyword, tag in KEYWORDS_TO_TAGS.items():
        if keyword.lower() in text.lower():
            tags.add(tag)
    return list(tags) if tags else ["General"]

@app.route("/", methods=["GET", "POST"])
def index():
    data = load_data()

    if request.method == "POST":
        text = request.form.get("thought")
        if text.strip():
            tags = auto_tag(text)
            entry = {
                "text": text,
                "tags": tags,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            data.append(entry)
            save_data(data)
        return redirect("/")

    # Group entries by tag
    grouped = {}
    for entry in reversed(data):  # Show latest first
        for tag in entry["tags"]:
            grouped.setdefault(tag, []).append(entry)

    return render_template("index.html", grouped=grouped)

if __name__ == "__main__":
    app.run(debug=True)
