"""Tests for the SFM function."""
import pandas as pd
from pyformanceanalytics.table import SFM


def test_sfm():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1 to SP500.TR": [0.0077, 0.3906, 0.3010, 0.4257, 0.4357, 0.0969, 0.6601, 0.0, 0.1132, 0.0408, 0.3604, 0.3521]
    }, index=["Alpha", "Beta", "Beta+", "Beta-", "R-squared", "Annualized Alpha", "Correlation", "Correlation p-value", "Tracking Error", "Active Premium", "Information Ratio", "Treynor Ratio"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert SFM(Ra, Rb).equals(expected_df)
