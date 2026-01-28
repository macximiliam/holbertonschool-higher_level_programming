#!/usr/bin/python3
"""
This script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Establishes connection to the database using command-line arguments.
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Creates a cursor object to interact with the database.
    cursor = db.cursor()

    # Executes the SQL query to filter states starting with 'N'.
    # Binary is used to ensure the 'N' is case-sensitive (Upper N).
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetches all matching rows and prints them.
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Closes the cursor and the database connection.
    cursor.close()
    db.close()
