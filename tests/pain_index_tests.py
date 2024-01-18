"""Tests for the PainIndex function."""
import pandas as pd
from pyformanceanalytics import PainIndex


def test_pain_index():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.015666286521955276],
    }, index=["Pain Index"])
    R = df[["HAM1"]]
    assert PainIndex(R).equals(expected_df)
