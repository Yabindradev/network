import sqlite3

# create a new database if one does not exist
conn = sqlite3.connect('mydatabase.db')

# create a cursor object
cursor = conn.cursor()

conn.execute('''CREATE TABLE IF NOT EXISTS  users
         (username  TEXT    NOT NULL);''')

# get user input
username = input('Enter your username: ')

# create a SQL query
query = 'SELECT * FROM users WHERE username = ?'

# execute the query
cursor.execute(query, (username,))

# get the result
result = cursor.fetchone()

# check if a username was returned
if result:
  print('Username already exists')
else:
  print('Username does not exist')
