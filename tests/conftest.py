import pytest
from f1.utils.conn import database_connection


@pytest.fixture
def conn():
    return database_connection()
