#!/usr/bin/python3
""" Start link class to table in database & inserts a new
    object/instance into the table """
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # create the  table(s)
    Base.metadata.create_all(engine)
    # create a configured "Session" class - else configure it yourself
    Session = sessionmaker(bind=engine)
    # create a session (to use), every interaction with the db requires one
    session = Session()
    # create an object
    new_state = State('Louisiana')
    # add the object to session
    session.add(new_state)
    # commit the session
    session.commit()
    # print the new object's id (confirms insertion to db)
    print(new_state.id)
    session.close()
