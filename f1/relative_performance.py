import logging as log

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from typing import Any
from utils.driver import get_driver_name
from .data import get_data


def relative_performance_chart(df: pd.DataFrame, driver_name: str) -> go.Figure | Any:
    """
    Generates a relative performance chart for the specified driver.

    Args:
        df (DataFrame): Dataframe containing the driver data.
        driver_name (str): Name of the driver.

    Returns:
        fig (go.Figure): Plotly Figure object with the polar chart.

    Raises:
        Exception: If there is an issue with the data or creating the Plotly graph.
    """
    try:
        if df.empty:
            log.error("DataFrame is empty.")
            return None

        df.fillna(0, inplace=True)
        df["position"] = df["position"].astype(int)
        df["position"] = 21 - df["position"]
        df["grid"] = 21 - df["grid"]

        pivot_df = df.pivot_table(
            index="driver_type",
            values=["wins", "position", "points", "grid", "fastest_lap"],
            aggfunc=np.mean,
        ).T

        if "points" in pivot_df.index:
            pivot_df.loc["points", :] = pivot_df.loc["points", :] / 25

        if "position" in pivot_df.index:
            pivot_df.loc["position", :] = pivot_df.loc["position", :] / 20

        if "grid" in pivot_df.index:
            pivot_df.loc["grid", :] = pivot_df.loc["grid", :] / 20

        fig = go.Figure()
        for i, column in enumerate(pivot_df.columns):
            name = driver_name if i == 0 else "team mate"
            fig.add_trace(
                go.Scatterpolar(
                    r=pivot_df[column].values,
                    theta=pivot_df.index,
                    fill="toself",
                    name=name,
                )
            )

        fig.update_layout(
            title="Relative Performance against Team Mate",
            polar=dict(radialaxis=dict(visible=False)),
            showlegend=True,
        )

        return fig
    except Exception as e:
        log.error("Failed to create the relative performance chart.", exc_info=True)
        raise


def relative_performance(driver_selection_id: int, conn) -> go.Figure:
    """
    Fetches the data and creates a relative performance chart for the specified driver.

    Args:
        driver_selection_id (str): The driver ID.
        conn: SQLAlchemy Engine instance.

    Returns:
        fig (go.Figure): Plotly Figure object with the polar chart.

    Raises:
        Exception: If there is an issue fetching the data or creating the Plotly graph.
    """
    try:
        db_query = "driver_comparison_query"
        df = get_data(db_query, driver_selection_id, conn)
        driver_name = get_driver_name(driver_selection_id, conn)
        return relative_performance_chart(df, driver_name)
    except Exception as e:
        log.error(
            "Failed to fetch data or create the relative performance charts.",
            exc_info=True,
        )
        raise
