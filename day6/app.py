from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            course TEXT
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()
    return render_template("list.html", data=data)


@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]

        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO students(name,course) VALUES (?,?)",(name,course))
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add.html")


@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        cur.execute("UPDATE students SET name=?, course=? WHERE id=?",
                    (name, course, id))
        conn.commit()
        conn.close()
        return redirect("/")

    cur.execute("SELECT * FROM students WHERE id=?", (id,))
    data = cur.fetchone()
    conn.close()
    return render_template("edit.html", data=data)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
