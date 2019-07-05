# import sqlite
import sqlite3

# create new db if not exists
conn = sqlite3.connect("cars.db")

# get cursor object
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE population
                (make TEXT, model TEXT, quantity INT)
                """)

# close db connection
conn.close()