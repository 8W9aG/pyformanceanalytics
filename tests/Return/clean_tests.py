"""Tests for the clean function."""
import pandas as pd
from pyformanceanalytics.Return import clean


def test_clean():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0074, 0.0193, 0.0155, -0.0091, 0.0076, -0.0039, -0.0231, 0.0395, 0.0147, 0.0288, 0.0156, 0.0176],
    }, index=df.index)
    R = df[["HAM1"]]
    assert clean(R).to_csv() == expected_df.to_csv()
