#!/usr/bin/python3
"""
This script adds a new State object named 'Louisiana'
to the database and prints its new ID.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup the connection to the database with the provided arguments.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Start a session to talk to the database.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for Louisiana.
    new_state = State(name="Louisiana")

    # Add the new state to the session and save it to the database.
    session.add(new_state)
    session.commit()

    # Print the ID that was automatically generated for the new state.
    print("{}".format(new_state.id))

    # Close the session.
    session.close()
