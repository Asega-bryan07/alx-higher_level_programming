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

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    '''
    prints the first State object from the database hbtn_0e_6_usa
    by taking the db arguments
    '''
    argv = sys.argv
    if len(argv) < 5 or ":" in argv[4]:
        exit(1)

    conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(argv[1], argv[2], argv[3]))
    session = sessionmaker(engine)

    Base.metadata.create_all(engine)
    session = Session()

    states = session.query(State).filter(State.name.like[argv[4]]).all()

    if len(states) == 0:
        print("Not found")
    else:
        print(states[0].id)

        session.close()
