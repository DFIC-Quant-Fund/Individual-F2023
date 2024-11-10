from AlgorithmImports import *
import pandas as pd
from io import StringIO
from datetime import datetime

class ShortInterestStrat(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2018, 1, 1)
        self.SetCash(10000)

        self.symbols = ['AAPL',  'LLY', 'AVGO', 'V', 'JPM', 'UNH', 'WMT', 'MA', 'JNJ', 'XOM', 'HD', 'PG', 'COST', 'ORCL', 'MRK', 'ABBV', 'AMD', 'ADBE', 'CRM', 'CVX', 'KO', 'BAC', 'PEP', 'MCD', 'TMO', 'NFLX', 'CSCO', 'INTC', 'ABT', 'TMUS', 'INTU','MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA']
        for symbol in self.symbols:
            self.AddEquity(symbol, Resolution.Daily).SetLeverage(5)

        self.short_interest_data = self.DownloadShortInterestData()
        self.last_trade_date = None

    def DownloadShortInterestData(self):
        file_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRCIXCPlV3azCe4v8twU2jtU6Iyq9iOp3lGcTbJumEBsfVgEhV_mIXEcHWVTeXnVnjnjiB13cE7JG2m/pub?gid=301598295&single=true&output=csv"
        file = self.Download(file_url)
        df = pd.read_csv(StringIO(file))
        df['Settlement Date'] = pd.to_datetime(df['Settlement Date'])

        short_interest_dict = {}
        for symbol in self.symbols:
            symbol_data = df[df['Symbol'] == symbol]
            short_interest_dict[symbol] = symbol_data
        return short_interest_dict

    def OnData(self, data):

        if self.last_trade_date is not None and self.last_trade_date == self.Time.date():
            return

        short_interest_ratios = {}
        for symbol in self.symbols:
            if symbol in self.short_interest_data:
                symbol_data = self.short_interest_data[symbol]
                filtered_data = symbol_data[symbol_data['Settlement Date'] <= self.Time].sort_values(by='Settlement Date', ascending=False)

                if not filtered_data.empty:
                    recent_data = filtered_data.head(1).iloc[0]
                    short_interest_ratio = recent_data['Short Interest Ratio']
                    short_interest_ratios[symbol] = short_interest_ratio

        if short_interest_ratios:
            sorted_stocks = sorted(short_interest_ratios.items(), key=lambda x: x[1])
            top_10_percent = int(0.1 * len(sorted_stocks))
            selected_stocks = [symbol for symbol, _ in sorted_stocks[:top_10_percent]]

            # Liquidatte stocks not in the selected list
            for invested_symbol in [x.Key.Value for x in self.Portfolio if x.Value.Invested]:
                if invested_symbol not in selected_stocks:
                    self.Liquidate(invested_symbol)

            # Invest equally in selected stocks
            for symbol in selected_stocks:
                self.SetHoldings(symbol, 1.0 / len(selected_stocks))

            self.last_trade_date = self.Time.date()