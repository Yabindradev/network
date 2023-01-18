import sqlite3 as db


conn = db.connect("User.db")
cur = conn.cursor()
conn.execute('''CREATE TABLE User
         (ID INT PRIMARY KEY     NOT NULL,
         Username           TEXT    NOT NULL);''')



conn.close()

