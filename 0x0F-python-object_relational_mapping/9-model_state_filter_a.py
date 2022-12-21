#!/usr/bin/python3
""" Start link class to table in database """
import sys
from model_state import Base, State

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
    # query State for all State objects that contain letter 'a'
    states = session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id)
    # see what the results are:
    for state in states:
        print(f'{state.id}:', state.name)
