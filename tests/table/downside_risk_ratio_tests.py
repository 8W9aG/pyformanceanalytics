"""Tests for the DownsideRiskRatio function."""
import pandas as pd
from pyformanceanalytics.table import DownsideRiskRatio

def test_downside_risk_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0178, 0.0617, 0.0078, 1.3581, 0.1567, 0.0106, 0.6721, 0.3581],
    }, index=[
            "monthly downside risk",
            "Annualised downside risk",
            "Downside potential",
            "Omega",
            "Sortino ratio",
            "Upside potential",
            "Upside potential ratio",
            "Omega-sharpe ratio"])
    R = df[["HAM1"]]
    assert DownsideRiskRatio(R).equals(expected_df)
