"""Tests for the DownsideRisk function."""
import pandas as pd
from pyformanceanalytics.table import DownsideRisk

def test_downside_risk():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0191, 0.0169, 0.0211, 0.0178, 0.0145, 0.0145, 0.1518, -0.0258, -0.0513, -0.0342, -0.0610],
    }, index=[
            "Semi Deviation",
            "Gain Deviation",
            "Loss Deviation",
            "Downside Deviation (MAR=10%)",
            "Downside Deviation (Rf=0%)",
            "Downside Deviation (0%)",
            "Maximum Drawdown",
            "Historical VaR (95%)",
            "Historical ES (95%)",
            "Modified VaR (95%)",
            "Modified ES (95%)"])
    R = df[["HAM1"]]
    assert DownsideRisk(R).equals(expected_df)
