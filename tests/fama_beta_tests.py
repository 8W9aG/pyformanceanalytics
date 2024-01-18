"""Tests for the FamaBeta function."""
import pandas as pd
from pyformanceanalytics import FamaBeta


def test_fama_beta():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "HAM1": [0.5351217289870001],
    }, index=["HAM1"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert FamaBeta(Ra, Rb).equals(expected_df)
