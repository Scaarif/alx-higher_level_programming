#!/usr/bin/python3
""" Start link class to table in database & lists all States and
corresponding City objects contained in the database hbtn_0e_101_usa """
import sys
from relationship_state import Base, State
# from model_state_and_city import Base, State, City
from relationship_city import City

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
    # query for State (state_cities: list of tuples)
    state_cities = session.query(State).order_by(State.id)
    # print (each result is a tuple of state.id, state.name & state.cities)
    for state_city in state_cities:
        print(f'{state_city.id}:', state_city.name)
        for city in state_city.cities:
            print(f'    {city.id}:', city.name)
