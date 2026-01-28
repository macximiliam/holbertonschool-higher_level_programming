#!/usr/bin/python3
"""
This script prints the first State object from the database.
It is a quick way to see the first entry in the table.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup the connection to the database with the user's info.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Start a session to communicate with the database.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get only the first state based on its ID.
    # We use .first() so we don't load all the data.
    first_state = session.query(State).order_by(State.id).first()

    # If we find a state, print it. If not, print Nothing.
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session to keep things tidy.
    session.close()
