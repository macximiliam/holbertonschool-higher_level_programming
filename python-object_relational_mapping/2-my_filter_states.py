#!/usr/bin/python3
"""
This script takes an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Establishes connection to the database using the first three arguments.
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Creates a cursor object to execute the search query.
    cursor = db.cursor()

    # Creates the SQL query using format with the fourth argument.
    # The query filters by state name and sorts results by id.
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        sys.argv[4]
    )
    cursor.execute(query)

    # Fetches and prints all matching rows.
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Closes the cursor and the database connection.
    cursor.close()
    db.close()
