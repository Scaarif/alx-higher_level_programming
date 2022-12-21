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
    # query the State
    state = session.query(State).first()
    # see what the results are:
    if state:
        print(f'{state.id}:', state.name)
    else:
        print('Nothing')
