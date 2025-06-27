#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the table."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: ./9-model_state_filter_a.py "
            "mysql_username mysql_password database_name"
        )
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

    # Query all states containing the letter 'a', ordered by id
    states_with_a = session.query(State).filter(State.name.like('%a%'))
    states_with_a = states_with_a.order_by(State.id).all()

    # Display results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()