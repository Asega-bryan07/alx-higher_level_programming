#!/usr/bin/python3
'''
 a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

 Your script should take 3 arguments: mysql username, mysql password and database name
 You must use the module SQLAlchemy
 You must import State and Base from model_state - from model_state import Base, State
 Your script should connect to a MySQL server running on localhost at port 3306
 Print the new states.id after creation
'''
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    new_inst = session.query(State).filter_by(name="Louisiana").first()
    print(new_inst.id)
    session.commit()
