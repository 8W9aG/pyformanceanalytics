"""Tests for the LCL function."""
import pandas as pd
from pyformanceanalytics.mean import LCL


def test_LCL():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.00670986771896018],
    }, index=["Lower Confidence Level"])
    R = df[["HAM1"]]
    assert LCL(R).equals(expected_df)
