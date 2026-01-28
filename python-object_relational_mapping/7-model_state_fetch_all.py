#!/usr/bin/python3
"""
This script lists all State objects from a database.
It uses SQLAlchemy to get the data easily.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Connect to the database using the info from the terminal arguments.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session to start working with the database.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get all states from the table and sort them by their ID.
    states = session.query(State).order_by(State.id).all()

    # Print each state found in the format "id: name".
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session when we are done.
    session.close()
