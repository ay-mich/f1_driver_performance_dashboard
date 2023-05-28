import logging as log
import pytest
import pandas as pd
from f1.utils.conn import database_connection

log.basicConfig(level=log.INFO)


def get_driver_id_on_selection(driver_select: str, conn) -> str:
    """
    Fetches the driver ID based on the driver selection.

    Args:
        driver_select (str): Selected driver name.
        conn: SQLAlchemy Engine instance.

    Returns:
        driver_id: The corresponding ID of the selected driver.

    Raises:
        Exception: If the SQL query fails.
    """
    conn = database_connection()
    try:
        sql = "SELECT driver_id from drivers WHERE driver_ref = %s"
        driver_id = pd.read_sql_query(sql, conn, params=(driver_select,)).iloc[0][0]
        return driver_id
    except Exception:
        log.error("Failed to fetch selected driver data.", exc_info=True)
        raise


def get_driver_list(conn) -> list:
    """
    Fetches the list of drivers from the database.

    Args:
        conn: SQLAlchemy Engine instance.

    Returns:
        driver_list: A list of all drivers.

    Raises:
        Exception: If the SQL query fails.
    """
    try:
        drivers_df = pd.read_sql_query("SELECT * FROM drivers", conn)
        driver_list = drivers_df["driver_ref"].unique().tolist()
        log.info("Fetched drivers list.")
        return driver_list
    except Exception:
        log.error("Failed to execute query on database.", exc_info=True)
        raise


def get_driver_name(driver_id: str, conn) -> str:
    """
    Fetches the driver name based on the driver ID.

    Args:
        driver_id (str): Driver ID.
        conn: SQLAlchemy Engine instance.

    Returns:
        driver_name: The corresponding name of the driver ID.

    Raises:
        Exception: If the SQL query fails.
    """
    try:
        driver_ref = pd.read_sql_query(
            "SELECT driver_ref FROM public_staging.stg_drivers WHERE driver_id = %s"
            % driver_id,
            conn,
        )
        return driver_ref["driver_ref"][0]
    except Exception:
        log.error("Failed to fetch driver name.", exc_info=True)
        raise


@pytest.mark.parametrize("driver_select, expected_driver_id", [("hamilton", 1)])
def test_get_driver_id_on_selection(driver_select, expected_driver_id, conn):
    driver_id = get_driver_id_on_selection(driver_select, conn)
    assert driver_id == expected_driver_id


@pytest.mark.parametrize("driver_id, expected_driver_name", [(1, "hamilton")])
def test_get_driver_name(driver_id, expected_driver_name, conn):
    driver_name = get_driver_name(driver_id, conn)
    assert driver_name == expected_driver_name


@pytest.mark.parametrize(
    "driver_id",
    [
        "hamilton",
        "verstappen",
        "leclerc",
    ],
)
def test_get_driver_list(driver_id, conn):
    driver_list = get_driver_list(conn)
    assert driver_list.count(driver_id) == 1
