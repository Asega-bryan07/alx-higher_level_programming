#!/usr/bin/python3
'''
script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
'''
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    '''
    updates the name of a State object from the database hbtn_0e_6_usa
    '''
    db_url = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
    .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(db_url)
    Session = sessionmaker(bind=db_url)

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    for i in session.query(State).filter(State.name.like('%a%')):
        session.delete(i)
        
    session.commit()

