#!/usr/bin/python3
'''
Script that defines the City class to work with the
MySQLAlchemy
'''
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """
    City class
        Attributes:
           __tablename__ (str): Table name of the class
           id (int): the id of the class
           name (str): name of the class
           state_id (int): state the city belongs to
     """
     __tablename__ = "cities"

     id = Colunm(Integer, primary_key=True)
     state_id = Column(Integer, ForeignKey('states_id'), nullable=False)
     name = Column(String(128), nullable=False)
