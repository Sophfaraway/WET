import sqlite3

conn = sqlite3.connect("hokus.db")

cursor = conn.cursor()

input_color = input("Add house color:")

cursor.execute(
    "INSERT INTO houses (color) VALUES (?)", (input_color,)
)
conn.commit()

cursor.execute("SELECT * FROM houses")
rows = cursor.fetchall()

for row in rows:
    print(row[1])

conn.close()