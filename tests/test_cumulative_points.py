import pandas as pd
import plotly.graph_objects as go
from unittest.mock import Mock, patch

from f1.cumulative_points import cumulative_points, cumulative_points_chart


# Test cumulative_points_chart function
def test_cumulative_points_chart():
    df = pd.DataFrame(
        {
            "date": pd.to_datetime(
                ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"]
            ),
            "driver_type": ["main", "main", "mate", "mate"],
            "points": [10, 20, 5, 15],
        }
    )
    driver_name = "hamilton"

    expected_fig = go.Figure()
    expected_fig.add_trace(
        go.Scatter(
            x=df[df["driver_type"] == "main"]["date"],
            y=df[df["driver_type"] == "main"]["cumulative_points"],
            mode="lines",
            name=driver_name,
        )
    )
    expected_fig.add_trace(
        go.Scatter(
            x=df[df["driver_type"] == "mate"]["date"],
            y=df[df["driver_type"] == "mate"]["cumulative_points"],
            mode="lines",
            name="team mate",
        )
    )
    expected_fig.update_layout(
        title="Cumulative Points Earned Over Time",
        xaxis_title="Date",
        yaxis_title="Cumulative Points Earned",
        showlegend=True,
    )

    fig = cumulative_points_chart(df, driver_name)

    assert fig == expected_fig


# Test cumulative_points function
@patch("f1.cumulative_points.get_data")
@patch("f1.cumulative_points.get_driver_name")
def test_cumulative_points(mock_get_driver_name, mock_get_data):
    driver_selection_id = 1
    conn = Mock()
    df = pd.DataFrame(
        {
            "date": pd.to_datetime(
                ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"]
            ),
            "driver_type": ["main", "main", "mate", "mate"],
            "points": [10, 20, 5, 15],
        }
    )
    driver_name = "hamilton"
    expected_fig = go.Figure()

    mock_get_data.return_value = df
    mock_get_driver_name.return_value = driver_name

    fig = cumulative_points(1, conn)

    assert fig == expected_fig
    mock_get_data.assert_called_once_with(
        "driver_comparison_query", driver_selection_id, conn
    )
    mock_get_driver_name.assert_called_once_with(driver_selection_id, conn)
