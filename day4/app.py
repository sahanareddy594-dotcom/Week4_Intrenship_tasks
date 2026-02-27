from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# create database & table if not exists
def init_db():
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            course TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO students(name,email,course) VALUES(?,?,?)",
                (name,email,course))
    conn.commit()
    conn.close()

    return redirect('/records')

@app.route('/records')
def records():
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()
    return render_template('records.html', data=data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
