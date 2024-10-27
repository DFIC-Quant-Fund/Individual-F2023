# Monte Carlo Project Proposal

# Introduction

Probability and statistics have long been used in the industry of trading and for good reason. The ability to model and predict certain outcomes allows us to reduce risk and calculate potential earnings. A specific and intuitive example of this concept is a Monte Carlo Simulation trade-bot.

# Summary

The strategy involves running hundreds or maybe even thousands of Monte Carlo simulations with each representing a potential market scenario for the next ~20 days. For each simulation, using data from the past 30 days, trends in the market, volatility, etc, a mean and standard deviation can be generated. These 2 pieces of information allow us to build a T-distribution for the following day and a random price can be selected to assign that day (<https://sci-hub.se/10.1177/031289627800300106>).

Continuing this pattern for the next ~20 days, we can conclude a single simulation by measuring its final price. Using hundreds or thousands of these simulations, a general overview of how all these variables might interact with each other can be seen and depending on the probability of desirable results with confidence intervals, a financial decision can be concluded. The simulations collectively offer a probabilistic view of potential market trajectories.

# Why this strategy is effective

Predicting the market is hard, if it were easy, everyone would be a billionaire. As humans, we can’t identify patterns and calculating the risk vs reward is inherently difficult. This is where Monte Carlo Strategies are effective. Using only math and statistics, we can get as close as possible to objectifying the market and our financial decisions. A particular reason as to why this is a strong strategy is Rigor. With an up to date bot, it can factor in current trends in the market, have access to statistical data that humans cannot intuitively understand, and use these quantities to make an objectively probabilistic decision.

#

# Potential Hazards

Some potential Hazards include the following:

1. **Weighing of constants:** If we notice that the market is heading up, the bot may increase its expected mean by a few dollars, however, if this is too high, it can change the probabilities far too much and it may be inaccurate. To counteract this, we want to invest in stocks that are not too volatile, the more predictable they are, the more successful this algorithm will be. This primarily includes healthcare, utilities, and customer staples (<https://luckboxmagazine.com/trades/volatility-by-sector/>)
2. **Sudden Changes:** With the lack of news and ability to see what may happen any unforeseen changes that are highly unlikely may render past data completely useless. A few solutions mitigate this risk such as the aforementioned non-volatile stocks, but also increasing the standard deviation of our dataset to a relatively safe number to account for these scenarios in the simulation

# Timeline

**Week 1.**

Develop a single run instance of a monte carlo simulation. This includes fetching data from past 30 days, generating the t-distribution, and running it to find out what a single simulation of the final result of the stock may be.

**Week 2.**

Create the full Monte Carlo simulation by running hundreds or thousands of the instances created above. With a list of final prices based on probability, analyze the data by finding the mean (either final or through each day), standard deviation, range, or any other pieces of information that may be helpful.

**Week 3.**

With a general idea of what the outcome may be, create a normal distribution with the gathered points. Using this distribution, perform risk assessment and determine the appropriate course of action based on future predictions. This can be done with confidence intervals.

**Week 4-5.**

Backtesting constants, and procedures to make them generally more accurate. Both overfitting and underfitting are concerns so finding the right balance is essential.