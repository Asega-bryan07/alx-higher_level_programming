#!/usr/bin/python3
"""
Session State file
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.arg[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
