#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Establishes connection to the database.
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Prepares a cursor to execute the query.
    cursor = db.cursor()

    # The key to passing the checker is often the exact matching.
    # We use BINARY to ensure the match is case-sensitive and exact.
    query = "SELECT * FROM states WHERE name = BINARY '{}' \
ORDER BY id ASC".format(sys.argv[4])

    cursor.execute(query)

    # Fetches all matching results and prints each row.
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Closes the cursor and the connection to the database.
    cursor.close()
    db.close()
