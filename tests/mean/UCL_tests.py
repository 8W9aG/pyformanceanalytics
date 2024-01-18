"""Tests for the UCL function."""
import pandas as pd
from pyformanceanalytics.mean import UCL


def test_UCL():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.015535586826494363],
    }, index=["Upper Confidence Level"])
    R = df[["HAM1"]]
    assert UCL(R).equals(expected_df)
