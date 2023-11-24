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
if __name__ == "__main__":
    '''
    script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
    '''
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    inp = sys.argv
    if len(inp) < 4:
        exit()

    conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
    session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)
    
    session = Session()
    
    my_query = session.query(State).order_by(State.id).all()
    
    for state in my_query:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))

    session.close()
