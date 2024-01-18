"""Tests for the sortDrawdowns function."""
import pandas as pd
from pyformanceanalytics import sortDrawdowns, findDrawdowns


def test_sort_drawdowns():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "return": [-0.02843684404562441, 0.0, 0.0],
        "from": [4.0, 1.0, 8.0],
        "trough": [7.0, 1.0, 8.0],
        "to": [8.0, 4.0, 13.0],
        "length": [5.0, 4.0, 6.0],
        "peaktotrough": [4.0, 1.0, 1.0],
        "recovery": [1.0, 3.0, 5.0],
    }, index=[2, 1, 3])
    R = df[["HAM1"]]
    assert sortDrawdowns(findDrawdowns(R)).to_csv() == expected_df.to_csv()
