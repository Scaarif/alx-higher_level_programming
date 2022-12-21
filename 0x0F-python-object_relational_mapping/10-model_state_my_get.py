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
    # query State for a state with the name passed in as argv[4]
    res = session.query(State.id).filter(State.name == sys.argv[4])
    # see what the results are:
    if (res.first()):
        print(res[0][0])
    else:
        print('Not found')
