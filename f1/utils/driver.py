import logging as log
import pandas as pd

log.basicConfig(level=log.INFO)


def get_driver_id_on_selection(driver_select: str, conn) -> int:
    """
    Fetches the driver ID based on the driver selection.

    Args:
        driver_select (str): Selected driver name.
        conn: SQLAlchemy Engine instance.

    Returns:
        driver_id (int): The corresponding ID of the selected driver.

    Raises:
        Exception: If the SQL query fails.
    """
    try:
        sql = "SELECT driver_id FROM drivers WHERE driver_ref = %s"
        driver_id = pd.read_sql_query(sql, conn, params=(driver_select,)).iloc[0][0]
        return driver_id
    except Exception as e:
        log.error("Failed to fetch selected driver data.", exc_info=True)
        raise


def get_driver_list(conn) -> list:
    """
    Fetches the list of drivers from the database.

    Args:
        conn: SQLAlchemy Engine instance.

    Returns:
        driver_list (list): A list of all drivers.

    Raises:
        Exception: If the SQL query fails.
    """
    try:
        drivers_df = pd.read_sql_query("SELECT * FROM drivers", conn)
        driver_list = drivers_df["driver_ref"].unique().tolist()
        log.info("Fetched drivers list.")
        return driver_list
    except Exception as e:
        log.error("Failed to execute query on database.", exc_info=True)
        raise


def get_driver_name(driver_id: int, conn) -> str:
    """
    Fetches the driver name based on the driver ID.

    Args:
        driver_id (int): Driver ID.
        conn: SQLAlchemy Engine instance.

    Returns:
        driver_name (str): The corresponding name of the driver ID.

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
    except Exception as e:
        log.error("Failed to fetch driver name.", exc_info=True)
        raise
