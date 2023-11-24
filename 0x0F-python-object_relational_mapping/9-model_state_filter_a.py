#!/usr/bin/python3
'''
script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    '''
    prints the first State object from the database hbtn_0e_6_usa
    by taking the db argument
    '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                (sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State).filter(State.name.like('%a%')):
        print(i.id, i.name, sep=": ")
