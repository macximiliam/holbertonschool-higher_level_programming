#!/usr/bin/python3
# This script connects to a MySQL database and lists all states from the database.
import MySQLdb
import sys

def list_states():
    # Connects to the database using arguments and executes a query to fetch all states.
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    cur = db.cursor()
    # Executes the SQL command to retrieve states sorted by ID
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
    cur.close()
    db.close()

if __name__ == "__main__":
    list_states()