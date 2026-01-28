#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a'
from the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Connect to the database using the arguments from the command line.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Start a session so we can talk to the database.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Find states with the letter 'a' and sort them by their ID.
    # We use '%a%' to look for 'a' anywhere in the name.
    states = session.query(State).filter(State.name.like('%a%')) \
                                 .order_by(State.id).all()

    # Print each state that matches our search.
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session to keep things clean.
    session.close()
