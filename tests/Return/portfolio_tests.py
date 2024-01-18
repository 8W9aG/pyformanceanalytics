"""Tests for the portfolio function."""
import pandas as pd
from pyformanceanalytics.Return import portfolio


def test_portfolio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "portfolio.returns": [0.007400000000000073, 0.019300000000000095, 0.01550000000000007, -0.009099999999999997, 0.007600000000000051, -0.0039000000000001256, -0.02310000000000001, 0.03950000000000009, 0.014699999999999935, 0.028799999999999937, 0.015600000000000058, 0.01760000000000006],
    }, index=df.index)
    R = df[["HAM1"]]
    assert portfolio(R).to_csv() == expected_df.to_csv()
