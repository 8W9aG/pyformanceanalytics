"""Tests for the CalculateReturns function."""
import pandas as pd
from pyformanceanalytics import CalculateReturns


def test_calculate_returns():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "HAM1": [None, 1.6081081081081083, -0.1968911917098446, -1.5870967741935484, -1.835164835164835, -1.513157894736842, 4.923076923076923, -2.7099567099567103, -0.6278481012658228, 0.9591836734693877, -0.45833333333333337, 0.12820512820512842],
    }, index=df.index)
    R = df[["HAM1"]]
    assert CalculateReturns(R).to_csv() == expected_df.to_csv()
