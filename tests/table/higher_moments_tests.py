"""Tests for the HigherMoments function."""
import pandas as pd
from pyformanceanalytics.table import HigherMoments


def test_higher_moments():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1 to SP500.TR": [0.0, 0.0, 0.3906, 0.5602, 0.4815],
    }, index=["CoSkewness", "CoKurtosis", "Beta CoVariance", "Beta CoSkewness", "Beta CoKurtosis"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert HigherMoments(Ra, Rb).equals(expected_df)
