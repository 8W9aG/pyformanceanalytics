"""Tests for the slope function."""
import pandas as pd
from pyformanceanalytics.CAPM.CML import slope


def test_slope():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "SP500.TR": [0.2000806434449863],
    }, index=["Capital Market Line Slope: SP500.TR"])
    R = df[["SP500 TR"]]
    assert slope(R).equals(expected_df)
