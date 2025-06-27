#!/usr/bin/python3
"""
Script to create a State ('California') and
a City ('San Francisco') in the hbtn_0e_100_usa database.
Uses SQLAlchemy for ORM mapping.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check if sufficient arguments are provided
    if len(sys.argv) != 4:
        print(
            "Usage: ./100-relationship_states_cities.py "
            "mysql_username mysql_password database_name"
        )
        sys.exit(1)

    # Set up the database connection
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/"
        f"{sys.argv[3]}"
    )

    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State and City instances
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add and commit the instances to the session
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Close the session
    session.close()