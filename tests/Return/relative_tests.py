"""Tests for the relative function."""
import pandas as pd
from pyformanceanalytics.Return import relative


def test_relative():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "HAM1/SP500.TR": [0.9742746615087041, 0.9839276354659883, 0.9896776087715047, 0.966464514173336, 0.949317259193852, 0.9420351881679576, 0.962831319649799, 0.9801813306982333, 0.9415790933063498, 0.9426786407099771, 0.8900933688221018, 0.9240553071958486],
    }, index=df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert relative(Ra, Rb).to_csv() == expected_df.to_csv()
