#!/usr/bin/python3
""" Defines a class, State and an instance Base = declarative_base() """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, String, Integer
from sqlalchemy.orm import relationship


Base = declarative_base()


#  define the class State
class State(Base):
    """ Defines the State class (with sqlalchemy datatypes )
    which defines the State table (to be created) """
    __tablename__ = 'states'  # the name of the table to be created
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade="all, delete, delete-orphan")

    def __init__(self, name):
        """ Initialize a State object/instance """
        self.name = name
