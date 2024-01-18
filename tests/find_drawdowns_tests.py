"""Tests for the findDrawdowns function."""
import pandas as pd
from pyformanceanalytics import findDrawdowns


def test_find_drawdowns():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "return": [0.0, -0.02843684404562441, 0.0],
        "from": [1.0, 4.0, 8.0],
        "trough": [1.0, 7.0, 8.0],
        "to": [4.0, 8.0, 13.0],
        "length": [4.0, 5.0, 6.0],
        "peaktotrough": [1.0, 4.0, 1.0],
        "recovery": [3.0, 1.0, 5.0],
    }, index=[1, 2, 3])
    R = df[["HAM1"]]
    assert findDrawdowns(R).to_csv() == expected_df.to_csv()
