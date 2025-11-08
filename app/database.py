from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os

load_dotenv()


# Load database Url from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the engine
engine = create_engine(
    DATABASE_URL, echo=True
)


# Create database tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Dependency for session
def get_session():
    with Session(engine) as session:
        yield session