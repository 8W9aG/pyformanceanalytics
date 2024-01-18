# pyformanceanalytics.CAPM

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Submodules

See each of these submodules for further documentation on their functions:

* [beta](beta/README.md)
* [CML](CML/README.md)
* [SML](SML/README.md)

## Functions

The following functions are supported:

### alpha

Calculate single factor model (CAPM) alpha

```python
from pyformanceanalytics.CAPM import alpha

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
alpha(Ra, Rb)
```

### RiskPremium

The CAPM Risk Premium on an investment is the measure of how much the asset’s performance
differs from the risk free rate

```python
from pyformanceanalytics.CAPM import RiskPremium

R = df[["SP500 TR"]]
RiskPremium(R)
```

### dynamic

Time-varying conditional single factor model beta

```python
from pyformanceanalytics.CAPM import dynamic

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
Z = df[["US 10Y TR", "US 3m TR"]]
dynamic(Ra, Rb, Z)
```

## epsilon

The regression epsilon is an error term measuring the vertical distance between the return predicted
by the equation and the real result

```python
from pyformanceanalytics.CAPM import epsilon

df = df[df.index.year = 1996]
Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
jensenAlpha(Ra, Rb)
```

## jensenAlpha

The Jensen’s alpha is the intercept of the regression equation in the Capital Asset Pricing Model
and is in effect the exess return adjusted for systematic risk.

```python
from pyformanceanalytics.CAPM import jensenAlpha

df = df[df.index.year = 1996]
Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
jensenAlpha(Ra, Rb)
```
