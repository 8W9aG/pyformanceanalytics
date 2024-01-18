"""Tests for the Variability function."""
import pandas as pd
from pyformanceanalytics.table import Variability


def test_variability():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0182, 0.0256, 0.0888]
    }, index=["Mean Absolute deviation", "monthly Std Dev", "Annualized Std Dev"])
    R = df[["HAM1"]]
    assert Variability(R).equals(expected_df)
