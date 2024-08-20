# NOTE: **************>>>>>>
#       - Install and use DB Browser for SQLite
#       - Create a Database named "idata.db", create table named events and ...

import sqlite3

connection = sqlite3.connect("idata.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM events WHERE band='Lions'")

rows = cursor.fetchall()

print(rows)