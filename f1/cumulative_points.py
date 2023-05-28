import logging as log

import pandas as pd
import plotly.graph_objects as go
import plotly.exceptions
from typing import Any
from utils.driver import get_driver_name
from .data import get_data


def cumulative_points_chart(df: pd.DataFrame, driver_name: str) -> go.Figure | Any:
    """
    Generates a cumulative points chart for the specified driver.

    Args:
        df (DataFrame): Dataframe containing the date, driver_type, and points.
        driver_name (str): Name of the driver.

    Returns:
        fig (go.Figure): Plotly Figure object with the line chart.

    Raises:
        pandas.core.common.PandasError: If there is an issue with the data.
        plotly.exceptions.PlotlyError: If there is an issue creating the Plotly graph.
    """
    try:
        df["date"] = pd.to_datetime(df["date"])
        df["cumulative_points"] = df.groupby("driver_type")["points"].cumsum()

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=df[df["driver_type"] == "main"]["date"],
                y=df[df["driver_type"] == "main"]["cumulative_points"],
                mode="lines",
                name=driver_name,
            )
        )
        fig.add_trace(
            go.Scatter(
                x=df[df["driver_type"] == "mate"]["date"],
                y=df[df["driver_type"] == "mate"]["cumulative_points"],
                mode="lines",
                name="team mate",
            )
        )
        fig.update_layout(
            title="Cumulative Points Earned Over Time",
            xaxis_title="Date",
            yaxis_title="Cumulative Points Earned",
            showlegend=True,
        )

        return fig
    except plotly.exceptions.PlotlyError as e:
        log.error(
            "Failed to create the cumulative points chart using Plotly.", exc_info=True
        )
        raise
    except Exception as e:
        log.error(
            "Failed to process the data for the cumulative points chart.", exc_info=True
        )
        raise


def cumulative_points(driver_selection_id: int, conn) -> go.Figure:
    """
    Fetches the data and creates a cumulative points chart for the specified driver.

    Args:
        driver_selection_id (str): The driver ID.
        conn: SQLAlchemy Engine instance.

    Returns:
        fig (go.Figure): Plotly Figure object with the line chart.

    Raises:
        Exception: If there is an issue fetching the data or creating the Plotly graph.
    """
    try:
        db_query = "driver_comparison_query"
        df = get_data(db_query, driver_selection_id, conn)
        driver_name = get_driver_name(driver_selection_id, conn)
        return cumulative_points_chart(df, driver_name)
    except Exception as e:
        log.error(
            "Failed to fetch data or create the cumulative points chart.", exc_info=True
        )
        raise
