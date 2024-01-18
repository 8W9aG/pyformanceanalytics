"""Tests for the ETL function."""
import pandas as pd
from pyformanceanalytics import ETL


def test_ETL():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "HAM1": [-0.024567840799934647],
    }, index=["ES"])
    R = df[["HAM1"]]
    assert ETL(R).equals(expected_df)
