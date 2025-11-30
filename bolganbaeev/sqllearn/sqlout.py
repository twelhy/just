import sqlite3
conn = sqlite3.connect("example.sql")
cur = conn.cursor()
cur.execute("SELECT * FROM users")
users = cur.fetchall()
for el in users:
    print(f"Name: {el[1]} \nPassword: {el[2]} \n\n")