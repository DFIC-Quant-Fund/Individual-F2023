
# Project Proposal

**Zayn Hu**

---

## Overview

Pairs trading is a market-neutral trading strategy that involves taking a long position in one asset while simultaneously taking a short position in another related or correlated asset. The goal of pairs trading is to profit from the relative price movements between the two assets, irrespective of the direction of the overall market.

## Hypothesis

Successful pairs trading relies on identifying assets that have a high historical correlation. Moreover, cointegration ensures that the relationship between the assets is stable over the long term, even if short-term divergences occur. Additionally, pairs trading assists in reducing trading risks brought on by movements in the market’s direction. Even if one underperforms, the other can compensate for the losses.

## Resources

- **Pairs trading:** <https://quantpedia.com/strategies/pairs-trading-with-stocks/>
- **ADF Test:** <https://blog.quantinsti.com/augmented-dickey-fuller-adf-test-for-a-pairs-trading-strategy/>
- **Distance Approach:** <https://www.youtube.com/watch?v=sKgDeqI39b4>
- **Correlation and Cointegration:** <https://quantstrategy.io/blog/understanding-correlations-and-cointegrations-for-effective-pairs-trading/>
- **Correlation, Cointegration and Stationarity:** <https://blog.quantinsti.com/pairs-trading-basics/>
- **Dataset:** <https://ca.finance.yahoo.com/>
- **Examples I viewed:** 
  - <https://github.com/AJeanis/Pairs-Trading>
  - <https://github.com/bideeen/Building-A-Trading-Strategy-With-Python>
  - <https://github.com/pkumeow/casestudy_on_Ashare_pair_trading>

## Timeline

- **Week 1:**
  - Research and get an overview of pairs trading
  - Review some strategies and examples

- **Week 2:**
  - Explore how to choose the pair of the stocks by using cointegration method
  - Test the stationarity by plotting the price ratio and price spread

- **Week 3:**
  - Creating a mean reversion strategy
  - Plot moving average price ratio in a short and a long window
  - Test if rolling Z-Scores could be used as trading indicators

- **Week 4:**
  - Creating buy and sell signals
  - Using ADF test to test the pair of stocks

- **Week 5:**
  - Risk and return factor neutrality
  - Using regression model to compute the beta of the chosen stocks with various benchmarks

- **Week 6:**
  - Simulation of the strategy
  - Calculating the price ratio and use if statements to execute trades
  - Track the position value every day and close the position if it exceeds the stoploss
  - Keeping track of a multitude of variables to analyze our performance
