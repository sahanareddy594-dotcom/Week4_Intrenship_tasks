import sqlite3
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT,
    status TEXT
)
""")

cursor.execute("INSERT INTO Users(name,email) VALUES('Sahana','sahana@gmail.com')")
cursor.execute("INSERT INTO Students(name,course) VALUES('Sydha','MCA')")
cursor.execute("INSERT INTO Tasks(task_name,status) VALUES('Create DB','Completed')")

conn.commit()

print("Users Table:")
for row in cursor.execute("SELECT * FROM Users"):
    print(row)

print("\nStudents Table:")
for row in cursor.execute("SELECT * FROM Students"):
    print(row)

print("\nTasks Table:")
for row in cursor.execute("SELECT * FROM Tasks"):
    print(row)


conn.close()
