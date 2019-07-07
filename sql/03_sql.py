import sqlite3

# conn = sqlite3.connect("new.db")

# cursor = conn.cursor()

# can use the 'with' keyword to make more compact
# line 9 replaces line 3
with sqlite3.connect("new.db") as connection:
    # replaces line 5
    c = connection.cursor()
    # replaces below
    c.execute("INSERT INTO population VALUES('New York City', 'NY', 8400000)")
    c.execute("INSERT INTO population VALUES('San Francisco', 'CA',  800000)")

# insert data
# cursor.execute("INSERT INTO population VALUES('New York         City',  'NY', 8400000)")

# cursor.execute("INSERT INTO population VALUES ('San Francisco',  'CA', 800000)")

connection.commit()

connection.close()

