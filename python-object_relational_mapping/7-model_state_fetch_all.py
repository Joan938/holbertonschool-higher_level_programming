#!/usr/bin/python3
"""Lists all State objects from the `states` table in `hbtn_0e_6_usa` DB."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: ./7-model_state_fetch_all.py "
            "mysql_username mysql_password database_name")
        sys.exit(1)

    # Extract arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the database
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost/{database_name}',
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print all states
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()