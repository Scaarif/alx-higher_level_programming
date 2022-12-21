#!/usr/bin/python3
""" Start link class to table in database & deletes all objects with
names containing the letter 'a' """
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
    # get the objects to delete & delete all (at once)
    session.query(State).filter(State.name.like("%a%"))\
        .delete(synchronize_session='fetch')
    # to delete a single object (use session.delete(obj))
    # commit the session
    session.commit()
    session.close()
