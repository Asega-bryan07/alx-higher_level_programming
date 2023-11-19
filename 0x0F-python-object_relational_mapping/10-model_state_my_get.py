#!/usr/bin/python3
'''
a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa

Your script should take 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
You can assume you have one record with the state name to search
Results must display the states.id
If no state has the name you searched for, display Not found
'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    '''
    prints the first State object from the database hbtn_0e_6_usa
    by taking the db arguments
    '''
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name == argv[4]).first())
    if states is not None:
	print("{0}".format(state.id))
    else:
        print("Not found")
