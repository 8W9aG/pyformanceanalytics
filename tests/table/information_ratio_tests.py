"""Tests for the InformationRatio function."""
import pandas as pd
from pyformanceanalytics.table import InformationRatio


def test_information_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0327, 0.1132, 0.3604]
    }, index=["Tracking Error", "Annualised Tracking Error", "Information Ratio"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert InformationRatio(Ra, Rb).equals(expected_df)
