#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
The script takes 3 arguments: mysql username, mysql password and database name.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connects to the database using the arguments provided in the command line.
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Creates a cursor object to execute SQL queries.
    cursor = db.cursor()

    # Executes the query to fetch all states ordered by id.
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetches all rows and prints them in the required format.
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Closes the cursor and the database connection.
    cursor.close()
    db.close()
