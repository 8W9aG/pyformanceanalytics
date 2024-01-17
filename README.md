# pyformanceanalytics

<a href="https://pypi.org/project/pyformance-analytics/">
    <img alt="PyPi" src="https://img.shields.io/pypi/v/pyformance-analytics">
</a>

A python wrapper around the [PerformanceAnalytics R package](https://github.com/braverock/PerformanceAnalytics).

## Dependencies :globe_with_meridians:

Python:

- [rpy2](https://rpy2.github.io/)
- [pandas](https://pandas.pydata.org/)
- [Pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html)
- numpy

R:

- [PerformanceAnalytics](https://github.com/braverock/PerformanceAnalytics)
- [ggplot2](https://ggplot2.tidyverse.org/)
- [gridExtra](https://cran.r-project.org/web/packages/gridExtra/index.html)

## Installation :inbox_tray:

This is a python package hosted on pypi, so to install simply run the following command:

`pip install pyformance-analytics`

## Usage example :eyes:

To get familiar with this wrapper you can first load an example dataset like so:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

It can now be used to run the following analytics functions:

### ActivePremium

```python
from pyformanceanalytics import active_premium

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
active_premium(Ra, Rb)
```

### AdjustedSharpeRatio

```python
from pyformanceanalytics import adjusted_sharpe_ratio

adjusted_sharpe_ratio(df)
```

### AppraisalRatio

```python
from pyformanceanalytics import appraisal_ratio

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
appraisal_ratio(Ra, Rb)
```

### AverageDrawdown

```python
from pyformanceanalytics import average_drawdown

average_drawdown(df)
```

### AverageLength

```python
from pyformanceanalytics import average_length

average_length(df)
```

### AverageRecovery

```python
from pyformanceanalytics import average_recovery

average_recovery(df)
```

### BernardoLedoitRatio

```python
from pyformanceanalytics import bernardo_ledoit_ratio

bernardo_ledoit_ratio(df)
```

### BetaCoVariance

```python
from pyformanceanalytics import beta_co_variance

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
beta_co_variance(Ra, Rb)
```

### BetaCoSkewness

```python
from pyformanceanalytics import beta_co_skewness

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
beta_co_skewness(Ra, Rb)
```

### BetaCoKurtosis

```python
from pyformanceanalytics import beta_co_kurtosis

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
beta_co_kurtosis(Ra, Rb)
```

### BurkeRatio

```python
from pyformanceanalytics import burke_ratio

burke_ratio(df)
```

### CalmarRatio

```python
from pyformanceanalytics import calmar_ratio

calmar_ratio(df)
```

### SterlingRatio

```python
from pyformanceanalytics import sterling_ratio

sterling_ratio(df)
```

### CAPM.alpha

```python
from pyformanceanalytics.CAPM import alpha

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
alpha(Ra, Rb)
```

### CAPM.beta

```python
from pyformanceanalytics.CAPM.beta import beta

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
beta(Ra, Rb)
```

### CAPM.beta.bull

```python
from pyformanceanalytics.CAPM.beta import bull

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
bull(Ra, Rb)
```

### CAPM.beta.bear

```python
from pyformanceanalytics.CAPM.beta import bear

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
bear(Ra, Rb)
```

### TimingRatio

```python
from pyformanceanalytics import timing_ratio

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
timing_ratio(Ra, Rb)
```

### CAPM.CML.slope

```python
from pyformanceanalytics.CAPM.CML import slope

Rb = df[["SP500 TR"]]
slope(Rb)
```

### CAPM.CML

```python
from pyformanceanalytics.CAPM.CML import CML

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
CML(Ra, Rb)
```

### CAPM.RiskPremium

```python
from pyformanceanalytics.CAPM.risk_premium import risk_premium

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
risk_premium(Ra, Rb)
```

### CAPM.SML.slope

```python
from pyformanceanalytics.CAPM.SML import slope

Rb = df[["SP500 TR"]]
slope(Rb)
```

### CAPM.dynamic

```python
from pyformanceanalytics.CAPM import dynamic

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
Z = df[["US 10Y TR", "US 3m TR"]]
dynamic(Ra, Rb, Z)
```

### CAPM.epsilon

```python
from pyformanceanalytics.CAPM import epsilon

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
epsilon(Ra, Rb)
```

### CAPM.jensenAlpha

```python
from pyformanceanalytics import jensen_alpha

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
jensen_alpha(Ra, Rb)
```

### CDD

```python
from pyformanceanalytics import CDD

CDD(df)
```

### chart.ACF

```python
from pyformanceanalytics.chart import ACF

ACF(df).show()
```

### chart.ACFplus

```python
from pyformanceanalytics.chart import ACF_plus

ACF_plus(df).show()
```

### chart.Bar

```python
from pyformanceanalytics.chart import bar

bar(df).show()
```

### chart.BarVaR

```python
from pyformanceanalytics.chart import bar_va_r

Ra = df[["HAM1"]]
bar_va_r(Ra).show()
```

### chart.Boxplot

```python
from pyformanceanalytics.chart import boxplot

boxplot(df).show()
```

### chart.CaptureRatios

```python
from pyformanceanalytics.chart import capture_ratios

Ra = df[["HAM1", "HAM2", "HAM3", "HAM4", "HAM5", "HAM6"]]
Rb = df[["EDHEC LS EQ"]]
capture_ratios(Ra, Rb).show()
```

### chart.Correlation

```python
from pyformanceanalytics.chart import correlation

correlation(df).show()
```

### chart.CumReturns

```python
from pyformanceanalytics.chart import cum_returns

cum_returns(df).show()
```

### chart.Drawdown

```python
from pyformanceanalytics.chart import drawdown

Ra = df[["HAM1"]]
drawdown(Ra).show()
```

### chart.ECDF

```python
from pyformanceanalytics.chart import ECDF

Ra = df[["HAM1"]]
ECDF(Ra).show()
```

### chart.Events

```python
import datetime
from pyformanceanalytics.chart import events

Ra = df[["HAM1"]]
events(Ra, [datetime.date(2006, 8, 31)]).show()
```

### chart.Histogram

```python
from pyformanceanalytics.chart import histogram

Ra = df[["HAM1"]]
histogram(Ra).show()
```

### chart.QQplot

```python
from pyformanceanalytics.chart import QQ_plot

Ra = df[["HAM2"]]
QQ_plot(Ra).show()
```

### chart.Regression

```python
from pyformanceanalytics.chart import regression

Ra = df[["HAM1", "HAM2"]]
Rb = df[["SP500 TR"]]
regression(Ra, Rb).show()
```

### chart.RelativePerformance

```python
from pyformanceanalytics.chart import relative_performance

Ra = df[["HAM1", "HAM2", "HAM3", "HAM4", "HAM5", "HAM6"]]
Rb = df[["SP500 TR"]]
relative_performance(Ra, Rb).show()
```

### chart.RiskReturnScatter

```python
from pyformanceanalytics.chart import risk_return_scatter

risk_return_scatter(df).show()
```

### chart.RollingCorrelation

```python
from pyformanceanalytics.chart import rolling_correlation

Ra = df[["HAM1", "HAM2", "HAM3", "HAM4", "HAM5", "HAM6"]]
Rb = df[["SP500 TR"]]
rolling_correlation(Ra, Rb).show()
```

### chart.RollingMean

```python
from pyformanceanalytics.chart import rolling_mean

rolling_mean(df).show()
```

### chart.RollingPerformance

```python
from pyformanceanalytics.chart import rolling_performance

rolling_performance(df).show()
```

### chart.RollingQuantileRegression

```python
from pyformanceanalytics.chart import rolling_quantile_regression

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
rolling_quantile_regression(Ra, Rb).show()
```

### chart.SnailTrail

```python
from pyformanceanalytics.chart import snail_trail

snail_trail(df).show()
```

### chart.StackedBar

```python
from pyformanceanalytics.chart import stacked_bar

stacked_bar(weights_df).show()
```

### chart.VaRSensitivity

```python
from pyformanceanalytics.chart import va_r_sensitivity

va_r_sensitivity(df).show()
```

### charts.PerformanceSummary

```python
from pyformanceanalytics.charts import performance_summary

performance_summary(df).show()
```

### charts.RollingPerformance

```python
from pyformanceanalytics.charts import rolling_performance

rolling_performance(df).show()
```

### CoSkewnessMatrix

```python
from pyformanceanalytics import co_skewness_matrix

co_skewness_matrix(df)
```

### CoKurtosisMatrix

```python
from pyformanceanalytics import co_kurtosis_matrix

co_kurtosis_matrix(df)
```

### CoVariance

```python
from pyformanceanalytics import co_variance

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
co_variance(Ra, Rb)
```

### CoSkewness

```python
from pyformanceanalytics import co_skewness

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
co_skewness(Ra, Rb)
```

### CoKurtosis

```python
from pyformanceanalytics import co_kurtosis

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
co_kurtosis(Ra, Rb)
```

### M3.MM

```python
from pyformanceanalytics.M3 import mm

mm(df)
```

### M4.MM

```python
from pyformanceanalytics.M4 import mm

mm(df)
```

### DownsideDeviation

```python
from pyformanceanalytics import downside_deviation

downside_deviation(df)
```

### DownsidePotential

```python
from pyformanceanalytics import downside_potential

downside_potential(df)
```

### SemiDeviation

```python
from pyformanceanalytics import semi_deviation

semi_deviation(df)
```

### SemiSD

```python
from pyformanceanalytics import semi_SD

semi_SD(df)
```

### SemiVariance

```python
from pyformanceanalytics import semi_variance

semi_variance(df)
```

### DownsideFrequency

```python
from pyformanceanalytics import downside_frequency

downside_frequency(df)
```

### DRatio

```python
from pyformanceanalytics import d_ratio

d_ratio(df)
```

### DrawdownDeviation

```python
from pyformanceanalytics import drawdown_deviation

drawdown_deviation(df)
```

### DrawdownPeak

```python
from pyformanceanalytics import drawdown_peak

Ra = df[["HAM1"]]
drawdown_peak(Ra)
```

### Drawdowns

```python
from pyformanceanalytics import drawdowns

drawdowns(df)
```

### findDrawdowns

```python
from pyformanceanalytics import find_drawdowns

Ra = df[["HAM1"]]
find_drawdowns(Ra)
```

### ETL

```python
from pyformanceanalytics import ETL

ETL(df)
```

### M2.ewma

```python
from pyformanceanalytics.M2 import ewma

ewma(df)
```

### M3.ewma

```python
from pyformanceanalytics.M3 import ewma

ewma(df)
```

### M4.ewma

```python
from pyformanceanalytics.M4 import ewma

ewma(df)
```

### FamaBeta

```python
from pyformanceanalytics import fama_beta

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
fama_beta(Ra, Rb)
```

### Frequency

```python
from pyformanceanalytics import frequency

frequency(df)
```

### HurstIndex

```python
from pyformanceanalytics import hurst_index

hurst_index(df)
```

### InformationRatio

```python
from pyformanceanalytics import information_ratio

Ra = df[["HAM1", "HAM2", "HAM3", "HAM4", "HAM5", "HAM6"]]
Rb = df[["SP500 TR"]]
information_ratio(Ra, Rb)
```

### Kappa

```python
from pyformanceanalytics import kappa

kappa(df, 0.005, 2)
```

### KellyRatio

```python
from pyformanceanalytics import kelly_ratio

kelly_ratio(df)
```

### kurtosis

```python
from pyformanceanalytics import kurtosis

kurtosis(df)
```

### lpm

```python
from pyformanceanalytics import lpm

lpm(df)
```

### M2Sortino

```python
from pyformanceanalytics import M2_sortino

Ra = df[["HAM1", "HAM2", "HAM3", "HAM4", "HAM5", "HAM6"]]
Rb = df[["SP500 TR"]]
M2_sortino(Ra, Rb, 0.005)
```

### MarketTiming

```python
from pyformanceanalytics import market_timing

Ra = df[["HAM1", "HAM2", "HAM3", "HAM4", "HAM5", "HAM6"]]
Rb = df[["SP500 TR"]]
market_timing(Ra, Rb)
```

### MartinRatio

```python
from pyformanceanalytics import martin_ratio

martin_ratio(df)
```

### maxDrawdown

```python
from pyformanceanalytics import max_drawdown

max_drawdown(df)
```

### M3.MCA

```python
from pyformanceanalytics.M3 import mca

mca(df.fillna(0.0))
```

### M4.MCA

```python
from pyformanceanalytics.M4 import mca

mca(df.fillna(0.0))
```

### mean.geometric

```python
from pyformanceanalytics.mean import geometric

geometric(df)
```

### mean.stderr

```python
from pyformanceanalytics.mean import stderr

stderr(df)
```

### mean.LCL

```python
from pyformanceanalytics.mean import lcl

lcl(df)
```

### mean.UCL

```python
from pyformanceanalytics.mean import ucl

ucl(df)
```

### MeanAbsoluteDeviation

```python
from pyformanceanalytics import mean_absolute_deviation

mean_absolute_deviation(df)
```

### MinTrackRecord

```python
from pyformanceanalytics import min_track_record

min_track_record(0.23, R=df[["HAM1"]])
```

### Modigliani

```python
from pyformanceanalytics import modigliani

Ra = df[["HAM1", "HAM2", "HAM3", "HAM4", "HAM5", "HAM6"]]
Rb = df[["SP500 TR"]]
modigliani(Ra, Rb)
```

### MSquared

```python
from pyformanceanalytics import m_squared

Ra = df[["HAM1", "HAM2", "HAM3", "HAM4", "HAM5", "HAM6"]]
Rb = df[["SP500 TR"]]
m_squared(Ra, Rb)
```

### MSquaredExcess

```python
from pyformanceanalytics import m_squared_excess

Ra = df[["HAM1", "HAM2", "HAM3", "HAM4", "HAM5", "HAM6"]]
Rb = df[["SP500 TR"]]
m_squared_excess(Ra, Rb)
```

### NetSelectivity

```python
from pyformanceanalytics import net_selectivity

Ra = df[["HAM1", "HAM2", "HAM3", "HAM4", "HAM5", "HAM6"]]
Rb = df[["SP500 TR"]]
net_selectivity(Ra, Rb)
```

### OmegaExcessReturn

```python
from pyformanceanalytics import omega_excess_return

Ra = df[["HAM1", "HAM2", "HAM3", "HAM4", "HAM5", "HAM6"]]
Rb = df[["SP500 TR"]]
omega_excess_return(Ra, Rb)
```

### OmegaSharpeRatio

```python
from pyformanceanalytics import omega_sharpe_ratio

omega_sharpe_ratio(df)
```

### PainIndex

```python
from pyformanceanalytics import pain_index

pain_index(df)
```

### PainRatio

```python
from pyformanceanalytics import pain_ratio

pain_ratio(df)
```

### ProbSharpeRatio

```python
from pyformanceanalytics import prob_sharpe_ratio

prob_sharpe_ratio(0.23, R=df[["HAM1"]])
```

### ProspectRatio

```python
from pyformanceanalytics import prospect_ratio

prospect_ratio(df)
```

### RachevRatio

```python
from pyformanceanalytics import rachev_ratio

rachev_ratio(df[["HAM1"]].fillna(0.0))
```

### Return.annualized

```python
from pyformanceanalytics.Return import annualized_

annualized_(df)
```

### Return.annualized.excess

```python
from pyformanceanalytics.Return.annualized import excess

Rp = df[["HAM1", "HAM2", "HAM3", "HAM4", "HAM5", "HAM6"]]
Rb = df[["SP500 TR"]]
excess(Rp, Rb)
```

### Return.calculate

```python
from pyformanceanalytics.Return import calculate

calculate(df)
```

### CalculateReturns

```python
from pyformanceanalytics import calculate_returns

calculate_returns(df)
```

### Return.centered

```python
from pyformanceanalytics.Return import centered

centered(df)
```

### centeredmoment

```python
from pyformanceanalytics import centeredmoment

centeredmoment(df, 2.0)
```

### centeredcomoment

```python
from pyformanceanalytics import centeredcomoment

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
centeredcomoment(Ra, Rb, 2.0, 3.0)
```

### Return.clean

```python
from pyformanceanalytics.Return import clean

clean(df)
```

### Return.convert

```python
from pyformanceanalytics.Return import convert

convert(df)
```

### Return.cumulative

```python
from pyformanceanalytics.Return import cumulative

cumulative(df)
```

### Return.excess

```python
from pyformanceanalytics.Return import excess

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
excess(Ra, Rb)
```

### Return.Geltner

```python
from pyformanceanalytics.Return import geltner

Ra = df[["HAM1"]]
geltner(Ra)
```

### Return.locScaleRob

```python
from pyformanceanalytics.Return import loc_scale_rob

loc_scale_rob(df)
```

### Return.portfolio

```python
from pyformanceanalytics.Return import portfolio

portfolio(df)
```

### Return.relative

```python
from pyformanceanalytics.Return import relative

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
relative(Ra, Rb)
```

### RPESE.control

```python
from pyformanceanalytics.RPESE import control

control("Mean")
```

### Selectivity

```python
from pyformanceanalytics import selectivity

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
selectivity(Ra, Rb)
```

### SharpeRatio

```python
from pyformanceanalytics import sharpe_ratio

sharpe_ratio(df)
```

### SharpeRatio.modified

```python
from pyformanceanalytics.SharpeRatio import modified

modified(df)
```

### SharpeRatio.annualized

```python
from pyformanceanalytics.SharpeRatio import annualized

annualized(df)
```

### M2.shrink

```python
from pyformanceanalytics.M2 import shrink

shrink(df)
```

### M3.shrink

```python
from pyformanceanalytics.M3 import shrink

shrink(df)
```

### M4.shrink

```python
from pyformanceanalytics.M4 import shrink

shrink(df)
```

### skewness

```python
from pyformanceanalytics import skewness

R = df[["HAM1"]]
skewness(R)
```

### SkewnessKurtosisRatio

```python
from pyformanceanalytics import skewness_kurtosis_ratio

R = df[["HAM1"]]
skewness_kurtosis_ratio(R)
```

### SmoothingIndex

```python
from pyformanceanalytics import smoothing_index

R = df[["HAM1"]]
smoothing_index(R)
```

### sortDrawdowns

```python
from pyformanceanalytics import find_drawdowns, sort_drawdowns

Ra = df[["HAM1"]]
drawdowns = find_drawdowns(Ra)
sort_drawdowns(drawdowns)
```

### SortinoRatio

```python
from pyformanceanalytics import sortino_ratio

sortino_ratio(df)
```

### SpecificRisk

```python
from pyformanceanalytics import specific_risk

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
specific_risk(Ra, Rb)
```

### StdDev

```python
from pyformanceanalytics import std_dev

std_dev(df)
```

### StdDev.annualized

```python
from pyformanceanalytics.StdDev import annualized

annualized(df)
```

### M2.struct

```python
from pyformanceanalytics.M2 import struct

struct(df)
```

### M3.struct

```python
from pyformanceanalytics.M3 import struct

struct(df)
```

### M4.struct

```python
from pyformanceanalytics.M4 import struct

struct(df)
```

### SystematicRisk

```python
from pyformanceanalytics import systematic_risk

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
systematic_risk(Ra, Rb)
```

### table.AnnualizedReturns

```python
from pyformanceanalytics.table import annualized_returns

annualized_returns(df)
```

### table.Arbitrary

```python
from pyformanceanalytics.table import arbitrary

arbitrary(df)
```

### table.Autocorrelation

```python
from pyformanceanalytics.table import autocorrelation

autocorrelation(df)
```

### table.CalendarReturns

```python
from pyformanceanalytics.table import calendar_returns

calendar_returns(df)
```

### table.CaptureRatios

```python
from pyformanceanalytics.table import capture_ratios

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
capture_ratios(Ra, Rb)
```

### table.UpDownRatios

```python
from pyformanceanalytics.table import up_down_ratios

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
up_down_ratios(Ra, Rb)
```

### table.Correlation

```python
from pyformanceanalytics.table import correlation

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
correlation(Ra, Rb)
```

### table.Distributions

```python
from pyformanceanalytics.table import distributions

distributions(df)
```

### table.DownsideRisk

```python
from pyformanceanalytics.table import downside_risk

downside_risk(df)
```

### table.DownsideRiskRatio

```python
from pyformanceanalytics.table import downside_risk_ratio

downside_risk_ratio(df)
```

### table.Drawdowns

```python
from pyformanceanalytics.table import drawdowns

drawdowns(df)
```

### table.DrawdownsRatio

```python
from pyformanceanalytics.table import drawdowns_ratio

drawdowns_ratio(df)
```

### table.HigherMoments

```python
from pyformanceanalytics.table import higher_moments

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
higher_moments(Ra, Rb)
```

### table.InformationRatio

```python
from pyformanceanalytics.table import information_ratio

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
information_ratio(Ra, Rb)
```

### table.ProbOutPerformance

```python
from pyformanceanalytics.table import prob_out_performance

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
prob_out_performance(Ra, Rb)
```

### table.RollingPeriods

```python
from pyformanceanalytics.table import rolling_periods

rolling_periods(df)
```

### table.TrailingPeriodsRel

```python
from pyformanceanalytics.table import trailing_periods_rel

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
trailing_periods_rel(Ra, Rb)
```

### table.SFM

```python
from pyformanceanalytics.table import sfm

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
sfm(Ra, Rb)
```

### table.SpecificRisk

```python
from pyformanceanalytics.table import specific_risk

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
specific_risk(Ra, Rb)
```

### table.Stats

```python
from pyformanceanalytics.table import stats

stats(df)
```

### table.Variability

```python
from pyformanceanalytics.table import variability

variability(df)
```

### TotalRisk

```python
from pyformanceanalytics import total_risk

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
total_risk(Ra, Rb)
```

### TrackingError

```python
from pyformanceanalytics import tracking_error

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
tracking_error(Ra, Rb)
```

### TreynorRatio

```python
from pyformanceanalytics import treynor_ratio

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
treynor_ratio(Ra, Rb)
```

### UlcerIndex

```python
from pyformanceanalytics import ulcer_index

ulcer_index(df)
```

### UpDownRatios

```python
from pyformanceanalytics import up_down_ratios

Ra = df[["HAM1"]]
Rb = df[["SP500 TR"]]
up_down_ratios(Ra, Rb)
```

### UpsideFrequency

```python
from pyformanceanalytics import upside_frequency

upside_frequency(df)
```

### UpsidePotentialRatio

```python
from pyformanceanalytics import upside_potential_ratio

upside_potential_ratio(df)
```

### UpsideRisk

```python
from pyformanceanalytics import upside_risk

upside_risk(df)
```

### VaR

```python
from pyformanceanalytics import var

var(R=df)
```

### VolatilitySkewness

```python
from pyformanceanalytics import volatility_skewness

volatility_skewness(df)
```

## License :memo:

The project is available under the [GPL2 License](LICENSE).
