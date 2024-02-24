from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

# Create an SQLite database engine
engine = create_engine('sqlite:///example.db', echo=True)

# Define metadata
metadata = MetaData()

# Define a table
users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

# Create the table in the database
metadata.create_all(engine)

# Insert data into the table
with engine.connect() as connection:
    connection.execute(users_table.insert(), [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ])

# Select data from the table
with engine.connect() as connection:
    result = connection.execute(users_table.select())
    for row in result:
        print(row)

