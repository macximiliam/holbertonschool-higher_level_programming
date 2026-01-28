#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
The script takes 3 arguments: mysql username, mysql password, and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connects to the database using the arguments provided.
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Creates a cursor to execute a single join query.
    cursor = db.cursor()

    # The query joins cities and states to display the state name.
    # We use only one execute() call as required.
    query = "SELECT cities.id, cities.name, states.name FROM cities \
JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)

    # Fetches all results and prints them in the required format.
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Clean up and close connection.
    cursor.close()
    db.close()
