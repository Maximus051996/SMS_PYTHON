from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Replace the placeholders with your own database details
db_username = "root"
db_password = "sugar123"
db_name = "testdb"


# Replace the placeholders with your own database details
DATABASE_URL=  f'mysql+pymysql://{db_username}:{db_password}@localhost/{db_name}'

# Create an engine object
engine = create_engine(
    DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# # Create a database object
# database = Database(DATABASE_URL)