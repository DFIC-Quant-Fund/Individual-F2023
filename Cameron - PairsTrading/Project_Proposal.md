**DFIC Quant Team – Individual Project Proposal**

**Overview**

Pairs trading is a quantitative trading strategy that involves identifying and trading pairs of highly correlated or cointegrated securities. The core idea is to capitalize on the temporary mispricing between these pairs, with the assumption that their price relationship will revert to the historical mean. This strategy is considered market-neutral, as it doesn't rely on the overall direction of the market.

**Correlation**: Extent to which two securities move in relation to each other. It ranges from -1 to 1, where 1 indicates a perfect positive relationship, -1 indicates a perfect negative relationship, and 0 implies no relationship at all.

**Cointegration**: Long-term equilibrium relationship between two or more time series (such as stock prices), where any deviation in the spread between them is expected to be temporary. This means that although the individual prices may diverge in the short term, they will likely revert back to a common trend over time.

**Hypothesis**

The hypothesis is based on the idea of mean reversion, where the spread between the prices of two correlated securities will eventually revert to its historical average. Market inefficiencies, such as temporary supply and demand imbalances, can cause deviations from this average, presenting opportunities for profit. The assumption is that these inefficiencies are temporary and the relationship between the pair will return to its long-term norm.

**Resources**

- Pair trading papers, historical stock prices and trends
- Example pair trading research frameworks and algorithms
- Online forums and websites such as QuantConnect and QuantPedia
  - <https://hudsonthames.org/definitive-guide-to-pairs-trading/>
  - <https://quantpedia.com/strategies/pairs-trading-with-stocks/>
  - <https://www.quantconnect.com/research/15300/pairs-trading-with-stocks>

**Timeline**

1. Initial Research (November Week 1, 2, 3, & 4)
    1. Study the concept of pairs trading, mean reversion, and cointegration
    2. Understand underlying math behind strategy and reasoning
2. Pair Discovery & Framework (December Week 1)
    1. Develop a testing framework to assess pair correlation and cointegration
    2. Research various pairs to test using the developed framework
3. Algorithm Development (December Week 2)
    1. Start developing the trading algorithm
    2. Incorporate logic for identifying trading signals and executing trades
4. Backtesting (December Week 3 & 4)
    1. Backtest the algorithm with historical data.
    2. Analyse performance and adjust strategy parameters as needed
5. Refinement & Additional Testing (December Week 4 & January Week 1)
    1. Refine the algorithm based on backtesting results
    2. Conduct further tests to ensure reliability and consistency
6. Documentation & Presentation (January Week 2)
    1. Document the research process, strategy development, and backtesting results
    2. Prepare a presentation to showcase the project findings and insights

A couple resources on Kalman Filter: [Video](https://www.youtube.com/watch?v=YavO2-sNVcs&t=540s&ab_channel=Hudson%26Thames), [QuantConnect Article](https://github.com/QuantConnect/Research/blob/master/Analysis/02%20Kalman%20Filter%20Based%20Pairs%20Trading.ipynb), [Simple Theory Article](https://www.quantstart.com/articles/Dynamic-Hedge-Ratio-Between-ETF-Pairs-Using-the-Kalman-Filter/)
