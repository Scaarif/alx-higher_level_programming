#!/usr/bin/python3
""" Defines a class, City and an instance Base = declarative_base() """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, String, Integer, ForeignKey
# from sqlalchemy.orm import relationship

from relationship_state import Base, State


class City(Base):
    """ Defines the City class (with sqlalchemy datatypes )
    which defines the City table (to be created) """
    __tablename__ = 'cities'  # the name of the table to be created
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name):
        """ Initialize City instance/object """
        self.name = name
