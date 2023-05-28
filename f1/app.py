import logging as log
import streamlit as st
from utils.conn import database_connection
from utils.driver import get_driver_id_on_selection, get_driver_list
from cumulative_points import cumulative_points
from relative_performance import relative_performance


def setup_logger():
    """
    Set up the logger with basic configurations.
    """
    log.basicConfig(level=log.INFO)


def connect_to_database():
    """
    Establish a connection to the database and return the connection object.

    Returns:
        conn: A connection object.
    """
    try:
        conn = database_connection()
        log.info("Database connection established successfully.")
        return conn
    except Exception as e:
        log.error("Failed to connect to the database.", e)
        raise


def render_dashboard(conn):
    """
    Render the Streamlit dashboard interface.

    Args:
        conn: A connection object.
    """
    st.title("F1 Driver Performance Dashboard")

    driver_list = get_driver_list(conn)
    driver_selected = st.sidebar.selectbox("Select a Driver:", driver_list)

    st.subheader(f"Selected Driver: {driver_selected}")
    st.sidebar.write("Your selected driver is compared against teammate(s)")

    driver_selection_id = get_driver_id_on_selection(driver_selected, conn)

    relative_performance_fig = relative_performance(driver_selection_id, conn)
    st.plotly_chart(relative_performance_fig)

    cumulative_points_fig = cumulative_points(driver_selection_id, conn)
    st.plotly_chart(cumulative_points_fig)


def main():
    setup_logger()
    conn = connect_to_database()
    render_dashboard(conn)
    log.info("Database connection closed.")


if __name__ == "__main__":
    main()
