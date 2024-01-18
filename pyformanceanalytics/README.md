# pyformanceanalytics

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Submodules

See each of these submodules for further documentation on their functions:

* [CAPM](CAPM/README.md)
* [chart](chart/README.md)
* [charts](charts/README.md)
* [M2](M2/README.md)
* [M3](M3/README.md)
* [M4](M4/README.md)
* [mean](mean/README.md)
* [Return](Return/README.md)
* [RPESE](RPESE/README.md)
* [SharpeRatio](SharpeRatio/README.md)
* [StdDev](StdDev/README.md)
* [table](table/README.md)

## Functions

The following functions are supported:

### ActivePremium

The return on an investment’s annualized return minus the benchmark’s annualized return.

```python
from pyformanceanalytics import ActivePremium

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
ActivePremium(Ra, Rb)
```

### AdjustedSharpeRatio

Adjusted Sharpe ratio was introduced by Pezier and White (2006) to adjusts for skewness and
kurtosis by incorporating a penalty factor for negative skewness and excess kurtosis.

```python
from pyformanceanalytics import AdjustedSharpeRatio

AdjustedSharpeRatio(df[df.index.year == 1996])
```

### AppraisalRatio

Appraisal ratio is the Jensen’s alpha adjusted for specific risk. The numerator is divided by specific
risk instead of total risk.

```python
from pyformanceanalytics import AppraisalRatio

df = df[df.index.year == 1996]
Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
AppraisalRatio(Ra, Rb)
```

### AverageDrawdown

Calculates the average depth of the observed drawdowns.

```python
from pyformanceanalytics import AverageDrawdown

AverageDrawdown(df)
```

### AverageLength

Calculates the average depth of the observed drawdowns.

```python
from pyformanceanalytics import AverageLength

AverageLength(df)
```

### AverageRecovery

Calculates the average length (in periods) of the observed recovery
period.

```python
from pyformanceanalytics import AverageRecovery

AverageRecovery(df)
```

### BernardoLedoitRatio

To calculate Bernardo and Ledoit ratio we take the sum of the subset of returns that are above 0 and
we divide it by the opposite of the sum of the subset of returns that are below 0

```python
from pyformanceanalytics import BernardoLedoitRatio

R = df[df.index.year == 1996][["HAM1"]]
BernardoLedoitRatio(R)
```

### BetaCoVariance

The covariance of a portfolios beta.

```python
from pyformanceanalytics import BetaCoVariance

Ra = df[["HAM2"]]
Rb = df[["SP500 TR"]]
BetaCoVariance(Ra, Rb)
```

### BetaCoSkewness

The coskewness of a portfolios beta.

```python
from pyformanceanalytics import BetaCoSkewness

Ra = df[["HAM2"]]
Rb = df[["SP500 TR"]]
BetaCoSkewness(Ra, Rb)
```

### BetaCoKurtosis

The cokurtosis of a portfolios beta.

```python
from pyformanceanalytics import BetaCoKurtosis

Ra = df[["HAM2"]]
Rb = df[["SP500 TR"]]
BetaCoKurtosis(Ra, Rb)
```

### BurkeRatio

To calculate Burke ratio we take the difference between the portfolio return and the risk free rate
and we divide it by the square root of the sum of the square of the drawdowns

```python
from pyformanceanalytics import BurkeRatio

R = df[df.index.year == 1996][["HAM1"]]
BurkeRatio(R)
```

### CalmarRatio

The Calmar ratio is a gauge of the performance of investment funds such as hedge funds and commodity trading advisors (CTAs)

```python
from pyformanceanalytics import CalmarRatio

R = df[["HAM1"]]
CalmarRatio(R)
```

### SterlingRatio

Sterling ratio is a risk-adjusted performance ratio that divides return of the portfolio by average portfolio drawdown over the period of analysis plus 10%

```python
from pyformanceanalytics import SterlingRatio

R = df[["HAM1"]]
SterlingRatio(R)
```

### TimingRatio

The TimingRatio may help assess whether the manager is a good timer of asset allocation decisions

```python
from pyformanceanalytics import TimingRatio

Ra = df[["HAM2"]]
Rb = df[["SP500 TR"]]
Rf = df[["US 3m TR"]]
TimingRatio(Ra, Rb, Rf=Rf)
```

### CDD

Calculate Uryasev’s proposed Conditional Drawdown at Risk (CDD
or CDaR) measure

```python
from pyformanceanalytics import CDD

CDD(df)
```

### CoSkewnessMatrix

Calculate the coskewness matrix between assets

```python
from pyformanceanalytics import CoSkewnessMatrix

R = df[["HAM1"]]
CoSkewnessMatrix(R)
```

### CoKurtosisMatrix

Calculate the cokurtosis matrix between assets

```python
from pyformanceanalytics import CoKurtosisMatrix

R = df[["HAM1"]]
CoKurtosisMatrix(R)
```

### CoVariance

Calculate the covariance between assets

```python
from pyformanceanalytics import CoVariance

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
CoVariance(Ra, Rb)
```

### CoSkewness

Calculate the coskewness between assets

```python
from pyformanceanalytics import CoSkewness

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
CoSkewness(Ra, Rb)
```

### CoKurtosis

Calculate the cokurtosis between assets

```python
from pyformanceanalytics import CoKurtosis

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
CoKurtosis(Ra, Rb)
```

### DownsideDeviation

Calculate the downside deviation of downside risk

```python
from pyformanceanalytics import DownsideDeviation

R = df[["HAM1"]]
DownsideDeviation(R)
```

### DownsidePotential

Calculate the downside potential of downside risk

```python
from pyformanceanalytics import DownsidePotential

R = df[["HAM1"]]
DownsidePotential(R)
```

### SemiDeviation

Calculate the semi deviation of downside risk

```python
from pyformanceanalytics import SemiDeviation

R = df[["HAM1"]]
SemiDeviation(R)
```

### SemiSD

Calculate the semi standard deviation of downside risk

```python
from pyformanceanalytics import SemiSD

R = df[["HAM1"]]
SemiSD(R)
```

### SemiVariance

Calculate the semi variance of downside risk

```python
from pyformanceanalytics import SemiVariance

R = df[["HAM1"]]
SemiVariance(R)
```

### DownsideFrequency

To calculate Downside Frequency, we take the subset of returns that are less than the target (or
Minimum Acceptable Returns (MAR)) returns and divide the length of this subset by the total
number of returns

```python
from pyformanceanalytics import DownsideFrequency

df = df[df.index.year == 1996]
R = df[["HAM1"]]
DownsideFrequency(R)
```

### DRatio

The d ratio is similar to the Bernado Ledoit ratio but inverted and taking into account the frequency
of positive and negative returns

```python
from pyformanceanalytics import DRatio

df = df[df.index.year == 1996]
R = df[["HAM1"]]
DRatio(R)
```

### DrawdownDeviation

Calculates a standard deviation-type statistic using individual drawdowns

```python
from pyformanceanalytics import DrawdownDeviation

R = df[["HAM1"]]
DrawdownDeviation(R)
```

### DrawdownPeak

Drawdown peak is for each return its drawdown since the previous peak

```python
from pyformanceanalytics import DrawdownPeak

DrawdownPeak(df)
```

### Drawdowns

A table showing the drawdowns

```python
from pyformanceanalytics import Drawdowns

R = df[["HAM1"]]
Drawdowns(df)
```

### findDrawdowns

A table showing the drawdowns with information

```python
from pyformanceanalytics import findDrawdowns

df = df[df.index.year == 1996]
R = df[["HAM1"]]
findDrawdowns(R)
```

### ETL

Calculates Expected Shortfall(ES) (also known as) Conditional Value at Risk(CVaR) or Expected
Tail Loss (ETL) for univariate, component, and marginal cases using a variety of analytical methods

```python
from pyformanceanalytics import ETL

R = df[["HAM1"]]
ETL(R)
```

### FamaBeta

Fama beta is a beta used to calculate the loss of diversification

```python
from pyformanceanalytics import FamaBeta

df = df[df.index.year == 1996]
Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
FamaBeta(Ra, Rb)
```

### Frequency

Gives the period of the return distribution

```python
from pyformanceanalytics import Frequency

R = df[["HAM1"]]
Frequency(R)
```

### HurstIndex

Hurst obtained a dimensionless statistical exponent by dividing the range by the standard deviation
of the observations, so this approach is commonly referred to as rescaled range (R/S) analysis

```python
from pyformanceanalytics import HurstIndex

R = df[["HAM1"]]
HurstIndex(R)
```

### InformationRatio

The Active Premium divided by the Tracking Error

```python
from pyformanceanalytics import InformationRatio

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
InformationRatio(Ra, Rb)
```

### Kappa

Introduced by Kaplan and Knowles (2004), Kappa is a generalized downside risk-adjusted perfor-
mance measure

```python
from pyformanceanalytics import Kappa

R = df[["HAM1"]]
Kappa(R, 0.005, 2)
```

### KellyRatio

Kelly criterion ratio (leverage or bet size) for a strategy

```python
from pyformanceanalytics import KellyRatio

R = df[["HAM1"]]
KellyRatio(R)
```

### kurtosis

Compute kurtosis of a univariate distribution

```python
from pyformanceanalytics import kurtosis

R = df[["HAM1"]]
kurtosis(R)
```

### lpm

Caclulate a Lower Partial Moment around the mean or a specified threshold

```python
from pyformanceanalytics import lpm

R = df[["HAM1"]]
lpm(R)
```

### M2Sortino

M squared for Sortino is a M^2 calculated for Downside risk instead of Total Risk

```python
from pyformanceanalytics import M2Sortino

df = df[df.index.year == 1996]
Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
M2Sortino(Ra, Rb, 0.0)
```

### MarketTiming

Allows to estimate Treynor-Mazuy or Merton-Henriksson market timing model

```python
from pyformanceanalytics import MarketTiming

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
MarketTiming(Ra, Rb)
```

### MartinRatio

Allows to estimate Treynor-Mazuy or Merton-Henriksson market timing model

```python
from pyformanceanalytics import MartinRatio

R = df[["HAM1"]]
MartinRatio(R)
```

### maxDrawdown

To find the maximum drawdown in a return series, we need to first calculate the cumulative returns
and the maximum cumulative return to that point

```python
from pyformanceanalytics import maxDrawdown

R = df[["HAM1"]]
maxDrawdown(R)
```

### MeanAbsoluteDeviation

To calculate Mean absolute deviation we take the sum of the absolute value of the difference be-
tween the returns and the mean of the returns and we divide it by the number of returns

```python
from pyformanceanalytics import MeanAbsoluteDeviation

R = df[["HAM1"]]
MeanAbsoluteDeviation(R)
```

### MinTrackRecord

The Minimum Track Record Length

```python
from pyformanceanalytics import MinTrackRecord

R = df[["HAM1"]]
MinTrackRecord(0.23, R=R)
```

### Modigliani

The Modigliani-Modigliani measure is the portfolio return adjusted upward or downward to match
the benchmark’s standard deviation

```python
from pyformanceanalytics import Modigliani

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
Modigliani(Ra, Rb)
```

### MSquared

M squared is a risk adjusted return useful to judge the size of relative performance between differents portfolios

```python
from pyformanceanalytics import MSquared

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
MSquared(Ra, Rb)
```

### MSquaredExcess

M squared excess is the quantity above the standard M

```python
from pyformanceanalytics import MSquaredExcess

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
MSquaredExcess(Ra, Rb)
```

### NetSelectivity

Net selectivity is the remaining selectivity after deducting the amount of return require to justify not
being fully diversified

```python
from pyformanceanalytics import NetSelectivity

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
NetSelectivity(Ra, Rb)
```

### Omega

Keating and Shadwick (2002) proposed Omega (referred to as Gamma in their original paper) as a
way to capture all of the higher moments of the returns distribution

```python
from pyformanceanalytics import Omega

R = df[["HAM1"]]
Omega(R)
```

### OmegaExcessReturn

Omega excess return is another form of downside risk-adjusted return

```python
from pyformanceanalytics import Omega

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
OmegaExcessReturn(Ra, Rb)
```

### OmegaSharpeRatio

The Omega-Sharpe ratio is a conversion of the omega ratio to a ranking statistic in familiar form to
the Sharpe ratio

```python
from pyformanceanalytics import OmegaSharpeRatio

R = df[["HAM1"]]
OmegaSharpeRatio(R)
```

### PainIndex

The pain index is the mean value of the drawdowns over the entire analysis period

```python
from pyformanceanalytics import PainIndex

R = df[["HAM1"]]
PainIndex(R)
```

### PainRatio

To calculate Pain ratio we divide the difference of the portfolio return and the risk free rate by the
Pain index

```python
from pyformanceanalytics import PainRatio

R = df[["HAM1"]]
PainRatio(R)
```

### ProbSharpeRatio

Given a predefined benchmark Sharpe ratio,the observed Sharpe Ratio can be expressed in probabilistic terms known as the Probabilistic Sharpe Ratio

```python
from pyformanceanalytics import ProbSharpeRatio

R = df[["HAM1"]]
R = df[["HAM1"]]
ProbSharpeRatio(0.23, R=R)
```

### ProspectRatio

Prospect ratio is a ratio used to penalise loss since most people feel loss greater than gain

```python
from pyformanceanalytics import ProspectRatio

R = df[["HAM1"]]
ProspectRatio(R)
```

### RachevRatio

RachevRatio computes the standard error of the Rachev ratio of the returns

```python
from pyformanceanalytics import RachevRatio

R = df[["HAM1"]]
RachevRatio(R)
```

### centeredmoment

Calculate the centered returns over an nth moment

```python
from pyformanceanalytics import centeredmoment

R = df[["HAM1"]]
centeredmoment(R)
```

### centeredcomoment

Calculate the centered returns over an nth comoment

```python
from pyformanceanalytics import centeredcomoment

df = df[df.index.year == 1996]
Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
centeredcomoment(Ra, Rb, 2.0, 2.0)
```

### Selectivity

Selectivity is the same as Jensen’s alpha

```python
from pyformanceanalytics import Selectivity

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
Selectivity(Ra, Rb)
```

### skewness

Compute skewness of a univariate distribution

```python
from pyformanceanalytics import skewness

R = df[["HAM1"]]
skewness(R)
```

### SkewnessKurtosisRatio

Skewness-Kurtosis ratio is the division of Skewness by Kurtosis

```python
from pyformanceanalytics import SkewnessKurtosisRatio

R = df[["HAM1"]]
SkewnessKurtosisRatio(R)
```

### SmoothingIndex

Proposed by Getmansky et al to provide a normalized measure of "liquidity risk."

```python
from pyformanceanalytics import SmoothingIndex

R = df[["HAM1"]]
SmoothingIndex(R)
```

### sortDrawdowns

Gives the drawdowns in order of worst to best

```python
from pyformanceanalytics import sortDrawdowns, findDrawdowns

df = df[df.index.year == 1996]
R = df[["HAM1"]]
sortDrawdowns(findDrawdowns(R))
```

### SortinoRatio

Sortino proposed an improvement on the Sharpe Ratio to better account for skill and excess performance by using only downside semivariance as the measure of risk

```python
from pyformanceanalytics import SortinoRatio

R = df[["HAM1"]]
SortinoRatio(R)
```

### SpecificRisk

Specific risk is the standard deviation of the error term in the regression equation

```python
from pyformanceanalytics import SpecificRisk

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
SpecificRisk(Ra, Rb)
```

### SystematicRisk

Systematic risk as defined by Bacon(2008) is the product of beta by market risk

```python
from pyformanceanalytics import SystematicRisk

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
SystematicRisk(Ra, Rb)
```

### TotalRisk

The square of total risk is the sum of the square of systematic risk and the square of specific risk

```python
from pyformanceanalytics import TotalRisk

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
TotalRisk(Ra, Rb)
```

### TrackingError

Tracking error is calculated by taking the square root of the average of the squared deviations
between the investment’s returns and the benchmark’s returns, then multiplying the result by the
square root of the scale of the returns

```python
from pyformanceanalytics import TrackingError

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
TrackingError(Ra, Rb)
```

### TreynorRatio

The Treynor ratio is similar to the Sharpe Ratio, except it uses beta as the volatility measure (to
divide the investment’s excess return over the beta)

```python
from pyformanceanalytics import TreynorRatio

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
TreynorRatio(Ra, Rb)
```

### UlcerIndex

Developed by Peter G. Martin in 1987 (Martin and McCann, 1987) and named for the worry caused
to the portfolio manager or investor

```python
from pyformanceanalytics import UlcerIndex

R = df[["HAM1"]]
UlcerIndex(R)
```

### UpDownRatios

Calculate metrics on how the asset in R performed in up and down markets, measured by periods
when the benchmark asset was up or down

```python
from pyformanceanalytics import UpDownRatios

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
UpDownRatios(Ra, Rb)
```

### UpsideFrequency

To calculate Upside Frequency, we take the subset of returns that are more than the target (or
Minimum Acceptable Returns (MAR)) returns and divide the length of this subset by the total
number of returns

```python
from pyformanceanalytics import UpsideFrequency

R = df[["HAM1"]]
UpsideFrequency(R)
```

### UpsidePotentialRatio

Sortino proposed an improvement on the Sharpe Ratio to better account for skill and excess perfor-
mance by using only downside semivariance as the measure of risk. That measure is the SortinoRatio.
This function, Upside Potential Ratio, was a further improvement, extending the measurement of
only upside on the numerator, and only downside of the denominator of the ratio equation

```python
from pyformanceanalytics import UpsidePotentialRatio

R = df[["HAM1"]]
UpsidePotentialRatio(R)
```

### UpsideRisk

Upside Risk is the similar of semideviation taking the return above the Minimum Acceptable Return
instead of using the mean return or zero

```python
from pyformanceanalytics import UpsideRisk

R = df[["HAM1"]]
UpsideRisk(R)
```

### VaR

Calculates Value-at-Risk(VaR) for univariate, component, and marginal cases using a variety of
analytical methods

```python
from pyformanceanalytics import VaR

R = df[["HAM1"]]
VaR(R)
```

### VolatilitySkewness

Volatility skewness is a similar measure to omega but using the second partial moment

```python
from pyformanceanalytics import VolatilitySkewness

R = df[["HAM1"]]
VolatilitySkewness(R)
```
