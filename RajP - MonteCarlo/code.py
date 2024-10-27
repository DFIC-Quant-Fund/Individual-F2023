# region imports
from AlgorithmImports import *
import numpy as np
from scipy import stats
import random
# endregion

class PensiveYellowElephant(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2023, 3, 25)
        self.SetEndDate(2023, 5, 25)
        self.SetCash(100000)
        self.symbol_list = ["IBM", "AMZN", "AXP", "ADBE"]
        self.port = [self.AddEquity(x, Resolution.Daily) for x in self.symbol_list]
        self.symbols = [x.Symbol for x in self.port]
        self.days = 20

    def OnData(self, data: Slice):
        if not any(symbol in data for symbol in self.symbols) or self.days == 0:
            return

        # getting financial data 
        prices = self.History(self.symbols, 30, Resolution.Daily)['close']
        prices_list = [prices[str(x) + " R735QTJ8XC9X"].tolist() for x in self.symbol_list]
        price_data = {i: lst for i, lst in zip(self.symbol_list, prices_list)}
        df = pd.DataFrame(price_data).pct_change()
        means = df.mean()
        covariances = df.cov()

        #monte carlo setup
        weights = np.array([0.25, 0.25, 0.25, 0.25])
        num_sims = 100
        time_frame = self.days
        self.days -= 1
        matrix_means = np.full(shape=(time_frame, len(self.symbol_list)), fill_value=means).T
        sims = np.full(shape=(time_frame, num_sims), fill_value=0)

        #cholesky decomp (multivariate normal distribution)
        for sim in range(num_sims):
            z_val = np.random.normal(size=(time_frame, len(self.symbol_list)))
            chol = np.linalg.cholesky(covariances)
            price_day = matrix_means + np.inner(chol, z_val)
            sims[:,sim] = np.cumprod(np.inner(weights, price_day.T)+1)*self.Portfolio.Cash
            matrix_means = np.full(shape=(time_frame, len(self.symbol_list)), fill_value=means).T

        
        # analyzing results and finding value at risk and cond value at risk
        results = pd.Series(sims[-1, :])
        var_percentile = np.percentile(results, 40)
        var = self.Portfolio.Cash - var_percentile
        b_var = results <= var_percentile
        cond_var = results[b_var].mean()
        cond_var_risk = self.Portfolio.Cash - cond_var

        def calc_bollinger_bands(prices, window_size=20, num_std_dev=2):
            rolling_mean = np.convolve(prices, np.ones(window_size)/window_size, mode='valid')
            rolling_std = np.std([prices[i:i+window_size] for i in range(len(prices)-window_size+1)], axis=1)
            upper_band = rolling_mean + num_std_dev * rolling_std
            lower_band = rolling_mean - num_std_dev * rolling_std
            return upper_band, lower_band

        def signals(data):
            upper, lower = calc_bollinger_bands(data)
            position = 0
            buys = []
            sells = []
            
            for i, price in enumerate(range(min(len(upper), len(lower), len(data), self.days))):
                # sell signal
                if data[i] > upper[i] and position == 1:
                    position = 0
                    sells.append(data[i])
                    buys.append(np.nan)
                # buy signal
                elif data[i] < lower[i] and position == 0:
                    position = 1
                    buys.append(data[i])
                    sells.append(np.nan)
                else:
                    buys.append(np.nan)
                    sells.append(np.nan)
            return calculate_profit(data, buys, sells), upper, lower

        def calculate_profit(data, buys, sells):
            # overall profit on a really basic strategy
            # 
            position = 0
            cash = 100000
            for i in range(min(len(buys), len(sells))):
                if not np.isnan(buys[i]):
                    position += cash // data[i]
                    cash -= position * data[i]
                elif not np.isnan(sells[i]):
                    cash += position * data[i]
                    position = 0
            if position > 0:
                cash += position * data[-1]
                position = 0
            return cash - self.Portfolio.Cash


        profits = []
        lower_bands = []
        upper_bands = []

        for sim in sims:
            profit, upper, lower = signals(sim)
            profits.append(profit)
            upper_nums = [value for value in upper if not np.isnan(value)]
            lower_nums = [value for value in lower if not np.isnan(value)]
            upper_bands.append(np.mean(upper_nums))
            lower_bands.append(np.mean(lower_nums))
        
        avg_profit = np.mean(profits)
        lower_avg = np.mean(lower_bands)
        upper_avg = np.mean(upper_bands)

        try:
            if avg_profit > var:
                for symbol in self.symbols:
                    self.SetHoldings(symbol, avg_profit / (var*400))
                    
            else:
                for symbol in self.symbols:
                    self.SetHoldings(symbol, -1 * avg_profit / (var*400))
        except: 
            pass

