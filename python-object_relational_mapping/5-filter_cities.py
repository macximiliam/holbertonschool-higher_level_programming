#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
Safe from SQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Establishes connection to the database using provided arguments.
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Creates a cursor object.
    cursor = db.cursor()

    # The query joins cities and states, filtering by the state name.
    # We use a placeholder (%s) to prevent SQL injection.
    query = "SELECT cities.name FROM cities \
JOIN states ON cities.state_id = states.id \
WHERE states.name = BINARY %s ORDER BY cities.id ASC"

    # Executes the query passing the state name as a parameter.
    cursor.execute(query, (sys.argv[4],))

    # Fetches all rows.
    rows = cursor.fetchall()

    # Formats the output to display city names separated by commas.
    cities_list = [row[0] for row in rows]
    print(", ".join(cities_list))

    # Closes cursor and connection.
    cursor.close()
    db.close()
