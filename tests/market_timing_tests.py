"""Tests for the MarketTiming function."""
import pandas as pd
from pyformanceanalytics import MarketTiming


def test_market_timing():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "Alpha": [0.009447134072265771],
        "Beta": [0.3842396537120326],
        "Gamma": [-4.473256117919313],
    }, index=["HAM1 to SP500.TR"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert MarketTiming(Ra, Rb).equals(expected_df)
