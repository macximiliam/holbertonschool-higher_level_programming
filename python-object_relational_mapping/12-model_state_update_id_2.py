#!/usr/bin/python3
"""
This script changes the name of a State object in the database.
It specifically looks for the state with ID 2.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup the connection using the credentials from the arguments.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session to start the update process.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Find the specific state where the ID is 2.
    state_to_update = session.query(State).filter(State.id == 2).first()

    # If the state is found, change its name to New Mexico.
    if state_to_update:
        state_to_update.name = "New Mexico"
        # Commit the changes to save them permanently in the database.
        session.commit()

    # Close the session.
    session.close()
