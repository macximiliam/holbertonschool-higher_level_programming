#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, safely.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Establishes a secure connection to the MySQL database.
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Creates a cursor to interact with the database.
    cursor = db.cursor()

    # To prevent SQL injection, we use a placeholder (%s) and pass
    # the user input as a separate argument to the execute method.
    query = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    # Fetches results safely and prints them.
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Closes cursor and database connection.
    cursor.close()
    db.close()
