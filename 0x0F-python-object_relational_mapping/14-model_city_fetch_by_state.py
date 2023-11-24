#!/usr/bin/python3
'''
Python file similar to model_state.py named model_city.py that contains the class definition of a City.

City class:
    inherits from Base (imported from model_state)
    links to the MySQL table cities
    class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    class attribute name that represents a column of a string of 128 characters and can’t be null
    class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id
    You must use the module SQLAlchemy
    Next, write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:

    Your script should take 3 arguments: mysql username, mysql password and database name
    You must use the module SQLAlchemy
    You must import State and Base from model_state - from model_state import Base, State
    Your script should connect to a MySQL server running on localhost at port 3306
    Results must be sorted in ascending order by cities.id
    Results must be display as they are in the example below (<state name>: (<city id>) <city name>)
the codes should not be imported
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from mode_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
            (sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = session()
    for i in (session.query(State.name, City.id, City.name)
            .filter(State.id == City.state_id)):
        print(i[0] + ": (" + str(instance[1]) + ") " + i[2])
