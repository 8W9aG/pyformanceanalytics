"""Tests for the centered function."""
import pandas as pd
from pyformanceanalytics.Return import centered


def test_centered():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "HAM1": [-0.0034249999999999992, 0.008475000000000002, 0.004675, -0.019925, -0.0032249999999999996, -0.014724999999999999, -0.033925, 0.028675, 0.003875, 0.017974999999999998, 0.004775, 0.0067750000000000015],
    }, index=df.index)
    R = df[["HAM1"]]
    assert centered(R).to_csv() == expected_df.to_csv()
