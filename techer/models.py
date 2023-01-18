import sqlite3

# create a new database if one does not exist
conn = sqlite3.connect('sb.db')

# create a cursor object
cursor = conn.cursor()

conn.execute('''CREATE TABLE IF NOT EXISTS  users
         ( username   TEXT    NOT NULL);''')




# get user input
username = input('Enter your username: ')

# create a SQL query
query = 'INSERT INTO users (username) VALUES (?)'

# execute the query
cursor.execute(query, (username,))

# save the changes to the database
conn.commit()
