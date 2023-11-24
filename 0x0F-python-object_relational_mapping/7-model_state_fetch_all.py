#!/usr/bin/python3
'''
 a script that lists all State objects from the database hbtn_0e_6_usa

 Your script should take 3 arguments: mysql username, mysql password and database name
 You must use the module SQLAlchemy
 You must import State and Base from model_state - from model_state import Base, State
 Your script should connect to a MySQL server running on localhost at port 3306
 Results must be sorted in ascending order by states.id
'''
if __name__ == "__main__":
    from sys import argv
    from model.state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    '''
    lists all State objects from the database hbtn_0e_6_usa
    '''
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(argv[1], argv[2], argv[3])

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    
    output = session.query(State).order_by(State.id).all()
    for state in output:
        print('{}: {}'.format(state.id, state.name))

    session.close()
