import logging as log
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

log.basicConfig(level=log.INFO)

load_dotenv()


def database_connection():
    """
    Establishes a connection to the database and returns the engine.

    Returns:
        conn (sqlalchemy.engine.Engine): SQLAlchemy Engine instance.

    Raises:
        Exception: If it fails to connect to the database or the connection string is invalid.
    """
    # Retrieve database connection details from environment variables
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")

    print(f"DB_USER: {db_user}")
    print(f"DB_PASSWORD: {db_password}")

    try:
        # Create a SQLAlchemy engine for connecting to the database
        conn = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}")
        log.info("Successfully connected to the database.")
        return conn
    except Exception as e:
        log.error("Failed to connect to the database.", exc_info=True)
        raise


if __name__ == "__main__":
    database_connection()
