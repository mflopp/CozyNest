from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from .db_config import DB_URI
from .base_config import Base
from .reserved_records import init_reserved_records
from typing import Generator

# Create SQLAlchemy object for working with the database
db = SQLAlchemy()

# Create the engine for connecting to PostgreSQL using SQLAlchemy
engine = create_engine(DB_URI, echo=True)

# Create a session maker bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db(app: Flask) -> None:
    """
    Initialize the database for a Flask application by configuring
    the database URI and setting up the SQLAlchemy object.

    Args:
        app (Flask): The Flask application instance.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


def get_session() -> Generator[Session, None, None]:
    """
    Dependency for getting the current SQLAlchemy session.
    Creates a new session for interacting with the database,
    which is closed after use.

    Returns:
        Session: The SQLAlchemy session object.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def init_tables() -> None:
    """
    Initialize the database by creating all tables defined in the models.
    This function will create the tables if they don't exist already.
    It will print a message confirming the success or failure of the operation.
    """
    try:
        Base.metadata.create_all(bind=engine)
        db = next(get_session())
        init_reserved_records(db)
        print("Connected and tables created.")
    except Exception as e:
        print(f"Error creating tables: {e}")
