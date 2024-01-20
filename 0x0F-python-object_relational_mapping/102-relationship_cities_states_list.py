#!/usr/bin/python3
"""Script to list all State and corresponding City objects in the database"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.orm import aliased
    from relationship_city import City
    from relationship_state import Base, State
    from sys import argv

    db = {
        'drivername': 'mysql+mysqldb',
        'host': 'localhost',
        'port': '3306',
        'username': argv[1],
        'password': argv[2],
        'database': argv[3]
    }

    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}", pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    # Using aliased to differentiate between City and State instances in the query
    state_alias = aliased(State)
    for city, state in session.query(City, state_alias)\
                             .join(state_alias, City.state)\
                             .order_by(state_alias.id, City.id):
        print("{}: {} -> {}".format(state.id, state.name, city.name))

    session.close()
