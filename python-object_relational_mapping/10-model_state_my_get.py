#!/usr/bin/python3
"""
prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}?charset=utf8'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    state_name = sys.argv[4].capitalize()
    Session = sessionmaker(bind=engine)
    session = Session()
    found = False
    for state in session.query(State).order_by(State.id).all():
        if state_name == state.name:
            print("{}".format(state.id))
            found = True
    if not found:
        print("Not found")
    session.close()