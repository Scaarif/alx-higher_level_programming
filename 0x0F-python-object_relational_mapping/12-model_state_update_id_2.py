#!/usr/bin/python3
""" Start link class to table in database & updates the
    object/instance with id 2's name to Mexico """
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
    # get the object whose name to update: get(primary_key)
    the_state = session.query(State).get(2)
    # update/set its name to new name
    the_state.name = 'New Mexico'
    # add the the object to session
    session.add(the_state)
    # commit the session
    session.commit()
    session.close()
