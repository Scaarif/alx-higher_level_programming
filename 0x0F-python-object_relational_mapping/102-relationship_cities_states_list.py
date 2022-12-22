#!/usr/bin/python3
""" Start link class to table in database & lists all Cities and
corresponding State objects contained in the database hbtn_0e_101_usa """
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
    # query for City (state_cities: list of tuples)
    cities = session.query(City).order_by(City.id)
    # print (each result is a tuple of city.id, city.name & city.state)
    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')
