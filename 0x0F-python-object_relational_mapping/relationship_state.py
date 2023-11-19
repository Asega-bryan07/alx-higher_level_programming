#!/usr/bin/python3
'''
script that defines the state class and a base 
class to work with MySQLAlchemy
'''
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class State(Base):
    '''
    class City
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to
    '''
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
