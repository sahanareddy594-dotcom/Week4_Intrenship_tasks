import sqlite3
conn = sqlite3.connect("day3.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT
)
""")

cursor.execute("INSERT INTO Students(name,course) VALUES(?,?)", ("Sahana","BCA"))
cursor.execute("INSERT INTO Students(name,course) VALUES(?,?)", ("Ravi","BSc"))
conn.commit()
print("Inserted records successfully")

print("\nStudent Records:")
for row in cursor.execute("SELECT * FROM Students"):
    print(row)

cursor.execute("UPDATE Students SET course=? WHERE name=?", ("BCA Final Year","Sahana"))
conn.commit()
print("\nUpdated record")


cursor.execute("DELETE FROM Students WHERE name=?", ("Ravi",))
conn.commit()
print("Deleted record")

print("\nFinal Records:")
for row in cursor.execute("SELECT * FROM Students"):
    print(row)
conn.close()
