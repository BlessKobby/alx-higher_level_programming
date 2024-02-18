#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query to get all State objects and their corresponding City objects
    result = (session.query(State, City)
              .join(City, State.id == City.state_id)
              .order_by(State.id, City.id)
              .all())

    # Display results
    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
