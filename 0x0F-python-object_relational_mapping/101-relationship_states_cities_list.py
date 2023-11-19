#!/usr/bin/python3
'''
a script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module SQLAlchemy
The connection to your MySQL server must be to localhost on port 3306
You must only use one query to the database
You must use the cities relationship for all State objects
Results must be sorted in ascending order by states.id and cities.id
'''
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    '''
    script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
    '''

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    join_st = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state in join_st:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('{}: {}'.format(city.id, city.name))
