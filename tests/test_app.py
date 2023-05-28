# test_app.py
import pandas as pd
import logging as log
import plotly.graph_objects
from unittest.mock import Mock, patch

from f1.app import setup_logger, connect_to_database, render_dashboard, main


# Test setup_logger function
def test_setup_logger(caplog):
    setup_logger()
    with caplog.at_level(log.INFO):
        log.info("Test info log message.")
    assert "Test info log message." in caplog.text


# Test connect_to_database function
@patch("f1.app.database_connection")
def test_connect_to_database(mock_database_connection):
    mock_conn = Mock()
    mock_database_connection.return_value = mock_conn

    conn = connect_to_database()
    assert conn == mock_conn
    mock_database_connection.assert_called_once()


# Test main function
@patch("f1.app.setup_logger")
@patch("f1.app.connect_to_database")
@patch("f1.app.render_dashboard")
def test_main(mock_render_dashboard, mock_connect_to_database, mock_setup_logger):
    main()

    mock_setup_logger.assert_called_once()
    mock_connect_to_database.assert_called_once()
    mock_render_dashboard.assert_called_once()


import pytest
from f1.app import *


@pytest.fixture
def conn():
    return database_connection()


def test_setup_logger(conn):
    # Test that the logger is setup with the correct level.
    assert log.getLogger().level == log.INFO


def test_connect_to_database(conn):
    # Test that a connection to the database can be established.
    assert conn is not None


def test_render_dashboard(conn):
    # Test that the dashboard can be rendered without errors.
    render_dashboard(conn)


def test_get_driver_list(conn):
    # Test that the get_driver_list function returns a list of drivers.
    driver_list = get_driver_list(conn)
    assert len(driver_list) > 0


def test_get_driver_id_on_selection(conn):
    # Test that the get_driver_id_on_selection function returns the correct driver id.
    driver_selected = "hamilton"
    driver_id = get_driver_id_on_selection(driver_selected, conn)
    assert driver_id == 1


def test_relative_performance(conn):
    # Test that the relative_performance function returns a plotly figure.
    driver_selection_id = 1
    relative_performance_fig = relative_performance(driver_selection_id, conn)
    assert isinstance(relative_performance_fig, plotly.graph_objects.Figure)


def test_cumulative_points(conn):
    # Test that the cumulative_points function returns a plotly figure.
    driver_selection_id = 1
    cumulative_points_fig = cumulative_points(driver_selection_id, conn)
    assert isinstance(cumulative_points_fig, plotly.graph_objects.Figure)
