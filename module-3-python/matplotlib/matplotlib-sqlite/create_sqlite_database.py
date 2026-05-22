import sqlite3
#create a database
conn=sqlite3.connect("sms.db")
print("Database created successfully")
#close the connection
conn.close()