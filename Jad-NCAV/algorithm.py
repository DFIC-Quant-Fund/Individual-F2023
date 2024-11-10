# https://quantpedia.com/strategies/net-current-asset-value-effect/
#
# The investment universe consists of all stocks on the London Exchange. Companies with more than one class of ordinary shares and foreign companies 
# are excluded. Also excluded are companies on the lightly regulated markets and companies which belong to the financial sector. The portfolio of
# stocks is formed annually in July. Only those stocks with an NCAV/MV higher than 1.5 are included in the NCAV/MV portfolio. This Buy-and-hold
# portfolio is held for one year. Stocks are weighted equally.
#
# QC implementation changes:
#   - Instead of all listed stock, we select top 3000 stocks by market cap from QC stock universe.

#region imports
from AlgorithmImports import *
#endregion

class NetCurrentAssetValueEffect(QCAlgorithm):

    def Initialize(self):
        
        self.weights = {} # edit

        self.SetStartDate(2014, 1, 1)
        self.SetEndDate(2024, 1, 1)
        self.SetCash(100000) 

        self.symbol:Symbol = self.AddEquity('SPY', Resolution.Daily).Symbol
        
        self.coarse_count:int = 3000
        self.leverage:int = 3
        
        self.long:List[Symbol] = []
        
        self.selection_flag:bool = False
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction, self.FineSelectionFunction)
        self.Schedule.On(self.DateRules.MonthEnd(self.symbol), self.TimeRules.AfterMarketOpen(self.symbol), self.Selection)

    def OnSecuritiesChanged(self, changes:SecurityChanges) -> None:
        for security in changes.AddedSecurities:
            security.SetFeeModel(CustomFeeModel())
            security.SetLeverage(self.leverage)

    def CoarseSelectionFunction(self, coarse:List[CoarseFundamental]) -> List[Symbol]:
        if not self.selection_flag:
            return Universe.Unchanged
        
        selected:List[Symbol] = [x.Symbol for x in coarse if x.HasFundamentalData and x.Market == 'usa']

        return selected
    
    def FineSelectionFunction(self, fine:List[FineFundamental]) -> List[Symbol]:
        fine = [x for x in fine if x.EarningReports.BasicAverageShares.ThreeMonths > 0 and x.MarketCap != 0 and x.ValuationRatios.WorkingCapitalPerShare != 0]
        sorted_by_market_cap = sorted(fine, key = lambda x:x.MarketCap, reverse=True)
        top_by_market_cap = [x for x in sorted_by_market_cap[:self.coarse_count]]
        
        # NCAV/MV calc.
        self.long = [x.Symbol for x in top_by_market_cap if ((x.ValuationRatios.WorkingCapitalPerShare * x.EarningReports.BasicAverageShares.ThreeMonths) / x.MarketCap) > 1.5]
        
        return self.long
    
    def OnData(self, data:Slice) -> None:
        if not self.selection_flag:
            return
        self.selection_flag = False

        stocks_invested:List[Symbol] = [x.Key for x in self.Portfolio if x.Value.Invested]
        for symbol in stocks_invested:
            if symbol not in self.long:
                self.Liquidate(symbol)

        
        total_npv = sum(self.weights.values()) # edit

        for symbol in self.long:
            if symbol in data and data[symbol]:
                weight = self.weights[symbol] / total_npv if total_npv != 0 else 1 # edit
                # self.SetHoldings(symbol, 1 / len(self.long))
                self.SetHoldings(symbol, weight) # edit

        self.long.clear()
    
    def Selection(self):
        if self.Time.month % 6 == 0: # edit
            self.selection_flag = True

# Custom fee model.
class CustomFeeModel(FeeModel):
    def GetOrderFee(self, parameters):
        fee = parameters.Security.Price * parameters.Order.AbsoluteQuantity * 0.00005
        return OrderFee(CashAmount(fee, "USD"))