#!/usr/bin/python3
"""
This script prints all City objects from the database.
It shows the state name and city details together.
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup the connection to the database.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Open a session to get the data.
    Session = sessionmaker(bind=engine)
    session = Session()

    # We query both State and City, joining them by their common ID.
    # The results are sorted by city ID.
    results = session.query(State, City).join(City).order_by(City.id).all()

    # Format and print: <state name>: (<city id>) <city name>
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session.
    session.close()
