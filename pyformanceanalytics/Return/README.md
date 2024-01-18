# pyformanceanalytics.Return

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Submodules

See each of these submodules for further documentation on their functions:

* [annualized](annualized/README.md)

## Functions

The following functions are supported:

### calculate

Calculate simple or compound returns from prices

```python
from pyformanceanalytics.Return import calculate

df = df[df.index.year == 1996]
R = df[["HAM1"]]
calculate(R)
```

### centered

Calculate centered returns

```python
from pyformanceanalytics.Return import centered

df = df[df.index.year == 1996]
R = df[["HAM1"]]
centered(R)
```

### clean

A function that provides access to multiple methods for cleaning outliers from return data

```python
from pyformanceanalytics.Return import clean

df = df[df.index.year == 1996]
R = df[["HAM1"]]
clean(R)
```

### cumulative

This is a useful function for calculating cumulative return over a period of time, say a calendar year

```python
from pyformanceanalytics.Return import cumulative

R = df[["HAM1"]]
cumulative(R)
```

### excess

Calculates the returns of an asset in excess of the given "risk free rate" for the period

```python
from pyformanceanalytics.Return import excess

df = df[df.index.year == 1996]
R = df[["HAM1"]]
excess(R)
```

### Geltner

David Geltner developed a method to remove estimating or liquidity bias in real estate index returns

```python
from pyformanceanalytics.Return import Geltner

df = df[df.index.year == 1996]
R = df[["HAM1"]]
Geltner(R)
```

### locScaleRob

locScaleRob returns the data after passing through a robust location and scale filter

```python
from pyformanceanalytics.Return import locScaleRob

df = df[df.index.year == 1996]
R = df[["HAM1"]]
locScaleRob(R)
```

### portfolio

Using a time series of returns and any regular or irregular time series of weights for each asset, this
function calculates the returns of a portfolio with the same periodicity of the returns data

```python
from pyformanceanalytics.Return import portfolio

df = df[df.index.year == 1996]
R = df[["HAM1"]]
portfolio(R)
```

### relative

Calculates the ratio of the cumulative performance for two assets through time

```python
from pyformanceanalytics.Return import portfolio

df = df[df.index.year == 1996]
Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
relative(Ra, Rb)
```
