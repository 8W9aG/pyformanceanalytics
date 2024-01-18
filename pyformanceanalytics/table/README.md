# pyformanceanalytics.table

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Functions

The following functions are supported:

### AnnualizedReturns

Table of Annualized Return, Annualized Std Dev, and Annualized Sharpe

```python
from pyformanceanalytics.table import AnnualizedReturns

R = df[["HAM1"]]
AnnualizedReturns(R)
```

### Arbitrary

This function creates a table of statistics from vectors of functions and labels passed in

```python
from pyformanceanalytics.table import Arbitrary

R = df[["HAM1"]]
Arbitrary(R)
```

### Autocorrelation

Produces data table of autocorrelation coefficients ρ and corresponding Q(6)-statistic for each column in R

```python
from pyformanceanalytics.table import Autocorrelation

R = df[["HAM1"]]
Autocorrelation(R)
```

### CalendarReturns

Returns a table of returns formatted with years in rows, months in columns, and a total column in
the last column

```python
from pyformanceanalytics.table import CalendarReturns

R = df[["HAM1"]]
CalendarReturns(R)
```

### CaptureRatios

Returns a table of returns formatted with years in rows, months in columns, and a total column in
the last column

```python
from pyformanceanalytics.table import CaptureRatios

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
CaptureRatios(Ra, Rb)
```

### UpDownRatios

Create a table that captures up/down ratios

```python
from pyformanceanalytics.table import UpDownRatios

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
UpDownRatios(Ra, Rb)
```

### Correlation

Calculate correlation and significance against each column of the data provided

```python
from pyformanceanalytics.table import Correlation

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
Correlation(Ra, Rb)
```

### Distributions

Table of standard deviation, Skewness, Sample standard deviation, Kurtosis, Excess kurtosis, Sample Skweness and Sample excess kurtosis

```python
from pyformanceanalytics.table import Distributions

R = df[["HAM1"]]
Distributions(R)
```

### DownsideRisk

Creates a table of estimates of downside risk measures for comparison across multiple instruments
or funds.

```python
from pyformanceanalytics.table import DownsideRisk

R = df[["HAM1"]]
DownsideRisk(R)
```

### DownsideRiskRatio

Table of downside risk, Annualised downside risk, Downside potential, Omega, Sortino ratio, Up-
side potential, Upside potential ratio and Omega-Sharpe ratio

```python
from pyformanceanalytics.table import DownsideRiskRatio

R = df[["HAM1"]]
DownsideRiskRatio(R)
```

### Drawdowns

Creates table showing statistics for the worst drawdowns

```python
from pyformanceanalytics.table import Drawdowns

R = df[["HAM1"]]
Drawdowns(R)
```

### DrawdownsRatio

Table of Calmar ratio, Sterling ratio, Burke ratio, Pain index, Ulcer index, Pain ratio and Martin
ratio

```python
from pyformanceanalytics.table import DrawdownsRatio

R = df[["HAM1"]]
DrawdownsRatio(R)
```

### HigherMoments

Summary of the higher moements and Co-Moments of the return distribution

```python
from pyformanceanalytics.table import HigherMoments

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
HigherMoments(R)
```

### InformationRatio

Table of Tracking error, Annualised tracking error and Information ratio

```python
from pyformanceanalytics.table import InformationRatio

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
InformationRatio(Ra, Rb)
```

### ProbOutPerformance

Table of Outperformance Reporting vs Benchmark

```python
from pyformanceanalytics.table import ProbOutPerformance

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
ProbOutPerformance(Ra, Rb)
```

### RollingPeriods

A table of estimates of rolling period return measures

```python
from pyformanceanalytics.table import RollingPeriods

R = df[["HAM1"]]
RollingPeriods(R)
```

### SFM

Takes a set of returns and relates them to a benchmark return

```python
from pyformanceanalytics.table import SFM

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
SFM(Ra, Rb)
```

### SpecificRisk

Table of specific risk, systematic risk and total risk

```python
from pyformanceanalytics.table import SpecificRisk

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
SpecificRisk(Ra, Rb)
```

### Stats

Returns a basic set of statistics that match the period of the data passed in (e.g., monthly returns
will get monthly statistics, daily will be daily stats, and so on)

```python
from pyformanceanalytics.table import Stats

R = df[["HAM1"]]
Stats(R)
```

### Variability

Table of Mean absolute difference, period standard deviation and annualised standard deviation

```python
from pyformanceanalytics.table import Variability

R = df[["HAM1"]]
Variability(R)
```
