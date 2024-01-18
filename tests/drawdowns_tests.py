"""Tests for the Drawdowns function."""
import pandas as pd
from pyformanceanalytics import Drawdowns


def test_drawdowns():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0, 0.0, 0.0, -0.009099999999999997, -0.0015691599999998473, -0.005463040275999975, -0.02843684404562441, 0.0, 0.0, 0.0, 0.0, 0.0],
    }, index=df.index)
    R = df[["HAM1"]]
    assert Drawdowns(R).to_csv() == expected_df.to_csv()
