#!/usr/bin/python3
""" Start a link to database and creates the State "California" with
with the City "San Fransisco" from the database hbtn_0e_100_usa """
import sys
from relationship_state import Base, State
from relationship_city import City

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
    # create a State (California) and a City (San Fransisco)
    new_state = State('California')
    new_city = City('San Fransisco')
    # use the state relationship (backref'd) to update/assign state_id value
    new_city.state = new_state
    # add the object to session
    session.add_all([new_state, new_city])
    # commit the session
    session.commit()
    # print the new object's id (confirms insertion to db)
    # print(new_state.id, new_city.id)
    session.close()
