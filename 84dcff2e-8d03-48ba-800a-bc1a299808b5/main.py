#Type code here
from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.technical_indicators import RSI, EMA, SMA, MACD, MFI, BB
import random
import json

class TradingStrategy(Strategy):

    @property
    def assets(self):
        return ["AAPL", "MSFT"]

    @property
    def interval(self):
        return "1min"

    def run(self, data_functions):
        choice = random.choice(self.assets())

        allocation = {}
        for a in self.assets():
            allocation[a] = 0

        allocation[choice] = 100

        print(f"setting allocation {json.dumps(allocation)}")
        return TargetAllocation(allocation)