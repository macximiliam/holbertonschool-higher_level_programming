#!/usr/bin/python3
"""
This script finds the ID of a state based on the name 
passed as an argument. It is safe from SQL injection.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup connection to the database using command line arguments.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Start a session to interact with the database.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Search for the state that matches the name given in the 4th argument.
    # We use .first() because we only expect one result.
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # If the state exists, print its ID. Otherwise, print "Not found".
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session.
    session.close()
