# pyformanceanalytics.chart

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Functions

The following functions are supported:

### ACF

Creates an ACF chart

```python
from pyformanceanalytics.chart import ACF

R = df[["HAM1"]]
ACF(R).show()
```

![ACF](ACF.jpg "ACF")

### ACFplus

Creates an ACF plus chart

```python
from pyformanceanalytics.chart import ACFplus

R = df[["HAM1"]]
ACFplus(R).show()
```

![ACFplus](ACFplus.jpg "ACFplus")

### Bar

Creates a bar returns chart

```python
from pyformanceanalytics.chart import Bar

R = df[["HAM1"]]
Bar(R).show()
```

![Bar](Bar.jpg "Bar")

### BarVaR

Plots the periodic returns as a bar chart overlayed with a risk metric calculation

```python
from pyformanceanalytics.chart import BarVaR

R = df[["HAM1"]]
BarVaR(R).show()
```

![BarVaR](BarVaR.jpg "BarVaR")

### Boxplot

Creates a boxplot chart

```python
from pyformanceanalytics.chart import Boxplot

R = df[["HAM1"]]
Boxplot(R).show()
```

![Boxplot](Boxplot.jpg "Boxplot")

### CaptureRatios

Creates a boxplot chart

```python
from pyformanceanalytics.chart import CaptureRatios

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
CaptureRatios(Ra, Rb).show()
```

![CaptureRatios](CaptureRatios.jpg "CaptureRatios")

### Correlation

Scatter plot of Up Capture versus Down Capture against a benchmark

```python
from pyformanceanalytics.chart import Correlation

Correlation(df).show()
```

![Correlation](Correlation.jpg "Correlation")

### CumReturns

Chart that cumulates the periodic returns given and draws a line graph of the results as a "wealth
index".

```python
from pyformanceanalytics.chart import CumReturns

CumReturns(df).show()
```

![CumReturns](CumReturns.jpg "CumReturns")

### Drawdown

Chart that cumulates the periodic returns given and draws a line graph of the results as a "wealth
index".

```python
from pyformanceanalytics.chart import Drawdown

Drawdown(df).show()
```

![Drawdown](Drawdown.jpg "Drawdown")

### ECDF

Creates an emperical cumulative distribution function (ECDF) overlaid with a cumulative distribu-
tion function (CDF)

```python
from pyformanceanalytics.chart import ECDF

ECDF(df).show()
```

![ECDF](ECDF.jpg "ECDF")

### Events

Creates a time series plot where events given by a set of dates are aligned, with the adjacent prior
and posterior time series data plotted in order

```python
import datetime
from pyformanceanalytics.chart import Events

Ra = df[["HAM1"]]
Events(Ra, [datetime.date(2006, 8, 31)]).show()
```

![Events](Events.jpg "Events")

### Histogram

Create a histogram of returns, with optional curve fits for density and normal

```python
from pyformanceanalytics.chart import Histogram

Histogram(df).show()
```

![Histogram](Histogram.jpg "Histogram")

### QQPlot

Plot the return data against any theoretical distribution

```python
from pyformanceanalytics.chart import QQPlot

QQPlot(df).show()
```

![QQPlot](QQPlot.jpg "QQPlot")

### Regression

Uses a scatterplot to display the relationship of a set of returns to a market benchmark

```python
from pyformanceanalytics.chart import Regression

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
Regression(Ra, Rb).show()
```

![Regression](Regression.jpg "Regression")

### RelativePerformance

Plots a time series chart that shows the ratio of the cumulative performance for two assets at each
point in time and makes periods of under- or out-performance easier to see

```python
from pyformanceanalytics.chart import RelativePerformance

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
RelativePerformance(Ra, Rb).show()
```

![RelativePerformance](RelativePerformance.jpg "RelativePerformance")

### RiskReturnScatter

Creates a scatter chart of annualized returns versus annualized risk (standard deviation)
for comparing manager performance

```python
from pyformanceanalytics.chart import RiskReturnScatter

RiskReturnScatter(df).show()
```

![RiskReturnScatter](RiskReturnScatter.jpg "RiskReturnScatter")

### RollingCorrelation

Creates a chart of rolling correlation metrics in a line chart

```python
from pyformanceanalytics.chart import RollingCorrelation

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
RollingCorrelation(Ra, Rb).show()
```

![RollingCorrelation](RollingCorrelation.jpg "RollingCorrelation")

### RollingMean

Creates a rolling mean return chart

```python
from pyformanceanalytics.chart import RollingMean

RollingMean(df).show()
```

![RollingMean](RollingMean.jpg "RollingMean")

### RollingPerformance

Creates a chart of rolling performance metrics in a line chart

```python
from pyformanceanalytics.chart import RollingPerformance

RollingPerformance(df).show()
```

![RollingPerformance](RollingPerformance.jpg "RollingPerformance")

### RollingQuantileRegression

Creates a chart of relative regression performance through time

```python
from pyformanceanalytics.chart import RollingQuantileRegression

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
RollingQuantileRegression(Ra, Rb).show()
```

![RollingQuantileRegression](RollingQuantileRegression.jpg "RollingQuantileRegression")

### SnailTrail

A chart that shows rolling calculations of annualized return and annualized standard deviation have
proceeded through time

```python
from pyformanceanalytics.chart import SnailTrail

SnailTrail(df).show()
```

![SnailTrail](SnailTrail.jpg "SnailTrail")

### StackedBar

This creates a stacked column chart with time on the horizontal axis and values in categories

```python
from pyformanceanalytics.chart import StackedBar

StackedBar(weights_df).show()
```

![StackedBar](StackedBar.jpg "StackedBar")

### VaRSensitivity

Creates a chart of Value-at-Risk and/or Expected Shortfall estimates by confidence interval for
multiple methods

```python
from pyformanceanalytics.chart import VaRSensitivity

VaRSensitivity(df).show()
```

![VaRSensitivity](VaRSensitivity.jpg "VaRSensitivity")
