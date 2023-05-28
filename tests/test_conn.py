import pytest

from f1.utils.conn import database_connection


def test_database_connection_success():
    """
    Test that the `database_connection()` function can successfully connect to the database.
    """
    # Set up the test environment
    db_connection_string = "postgresql://f1_user:passwordf1@localhost/f1"

    # Call the `database_connection()` function
    conn = database_connection()

    # Assert that the connection is successful
    assert conn is not None
