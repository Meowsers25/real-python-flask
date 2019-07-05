# create SQLite3 database and table
# import sqlite library
import sqlite3

# create new database if it doesnt already exist
conn = sqlite3.connect("new.db")

# get a cursor object to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, popualtion INT)
                """)

# close dtatbase connection
conn.close()