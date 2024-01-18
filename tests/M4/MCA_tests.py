"""Tests for the MCA function."""
import pandas as pd
from pyformanceanalytics.M4 import MCA


def test_mca():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "M4mca": [2.2782526292477943e-06],
        "converged": [True],
        "iter": [1.0],
        "U": [1.0],
    }, index=[1])
    R = df[["HAM1"]]
    assert MCA(R).to_csv() == expected_df.to_csv()
