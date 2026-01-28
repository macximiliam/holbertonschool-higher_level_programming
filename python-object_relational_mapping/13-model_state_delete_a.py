#!/usr/bin/python3
"""
This script deletes all State objects with a name containing
the letter 'a' from the database.
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup the connection to the database.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Start a session to perform the deletion.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Find all states that have the letter 'a' in their name.
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')).all()

    # Loop through the results and delete each one.
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes to delete them forever from the database.
    session.commit()

    # Close the session.
    session.close()
