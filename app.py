from flask import Flask, render_template, request
import sqlite3
import csv

# Database setup
conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    email TEXT,
    breach TEXT
)
''')
conn.commit()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/check', methods=["POST"])
def check():
    email = request.form['email']

    breaches = []

    with open("breaches.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            dataset_email = row[0]
            breach_name = row[1]
            breach_year = row[2]

            if email == dataset_email:
                breaches.append(f"{breach_name} ({breach_year})")

    # Save to DB
    if not breaches:
        breaches = ["No Breach Found"]

# Save everything (both cases)
    for breach in breaches:
        cursor.execute("INSERT INTO logs VALUES (?, ?)", (email, breach))

    conn.commit()
    return render_template("result.html", email=email, breaches=breaches)
@app.route('/history')
def history():
    cursor.execute("SELECT * FROM logs")
    data = cursor.fetchall()

    # Count breaches
    breach_count = {}

    for row in data:
        breach = row[1]

        if breach in breach_count:
            breach_count[breach] += 1
        else:
            breach_count[breach] = 1

    return render_template("history.html", data=data, breach_count=breach_count)
@app.route('/clear')
def clear():
    cursor.execute("DELETE FROM logs")
    conn.commit()
    return "History Cleared Successfully"
app.run(debug=True, port=5001)