#!/usr/bin/python3
""" Start link class to table in database & lists all cities by state """
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # create a configured "Session" class - else configure it yourself
    Session = sessionmaker(bind=engine)
    # create a session (to use), every interaction with the db requires one
    session = Session()
    # query the State
    state_cities = session.query(City).join(State).order_by(City.id)
    # see what the results are:
    for state_city in state_cities:
        print(f'{state_city.id}:', state_city.name)
