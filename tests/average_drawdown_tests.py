"""Tests for the AverageDrawdown function."""
import pandas as pd
from pyformanceanalytics import AverageDrawdown


def test_average_drawdown():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.03300843011735661],
        "HAM2": [0.042924088888993406],
        "HAM3": [0.053156584340169434],
        "HAM4": [0.09648562967588424],
        "HAM5": [0.19679817514561077],
        "HAM6": [0.04259908683337896],
        "EDHEC.LS.EQ": [0.028025710469682094],
        "SP500.TR": [0.08453864088594906],
        "US.10Y.TR": [0.042653961178717156],
        "US.3m.TR": [0.0],
    }, index=["Average Drawdown"])
    assert AverageDrawdown(df).equals(expected_df)
