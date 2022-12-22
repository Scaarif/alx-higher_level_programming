#!/usr/bin/python3
""" Start link class to table in database & lists all cities by state """
import sys
from model_state import Base, State
# from model_state_and_city import Base, State, City
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
    # query for City name & id + State name (state_cities: list of tuples)
    state_cities = session.query(
        City.id, City.name, State.name).join(State).order_by(City.id)
    # print (each result is a tuple of city.id, city.name & state.name)
    for state_city in state_cities:
        print(f'{state_city[2]}: ({state_city[0]})', state_city[1])
