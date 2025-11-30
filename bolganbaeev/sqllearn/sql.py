import sqlite3
name = None

conn = sqlite3.connect('example.sql')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (int auto_creament primary key, name varchar(50), pass varchar(50))')
conn.commit()
cur.close()
conn.close()

name = input("Write Name: ")
passw = input("Write password: ")

conn = sqlite3.connect('example.sql')
cur = conn.cursor()
cur.execute(f"INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, passw))
conn.commit()
cur.close()
conn.close()
