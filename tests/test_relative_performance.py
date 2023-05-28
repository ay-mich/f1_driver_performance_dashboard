import pytest
import pandas as pd
import plotly.graph_objects as go

from f1.utils.driver import get_driver_name
from f1.data import get_data
from f1.relative_performance import relative_performance_chart, relative_performance


def test_relative_performance_chart_empty_df():
    """
    Test that the `relative_performance_chart()` function returns None if the input DataFrame is empty.
    """
    df = pd.DataFrame()
    assert relative_performance_chart(df, "sonny_no_f1") is None


def test_relative_performance_chart_valid_df():
    """
    Test that the `relative_performance_chart()` function returns a Plotly Figure object with the polar chart for a valid input DataFrame.
    """
    df = pd.DataFrame(
        {
            "driver_type": "main",
            "wins": [1, 2],
            "position": [1, 2],
            "points": [10, 20],
            "grid": [1, 2],
            "fastest_lap": [1, 2],
        }
    )
    fig = relative_performance_chart(df, "hamilton")
    assert isinstance(fig, go.Figure)


def test_relative_performance_invalid_driver_id():
    """
    Test that the `relative_performance()` function raises an exception if the input driver ID is invalid.
    """
    conn = None
    with pytest.raises(Exception):
        relative_performance(87878787, conn)
