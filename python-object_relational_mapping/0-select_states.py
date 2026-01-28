#!/usr/bin/env python3
# This script connects to a MySQL database and lists all states from hbtn_0e_0_usa.
import MySQLdb
import sys

def list_states():
    # Connects to the database using command-line arguments and fetches all states.
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        
        cur = db.cursor()
        # Executes the query to get all states ordered by id.
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        
        rows = cur.fetchall()
        for row in rows:
            print(row)
            
        cur.close()
        db.close()
    except Exception:
        pass

if __name__ == "__main__":
    list_states()