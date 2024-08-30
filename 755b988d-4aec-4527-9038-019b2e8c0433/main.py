from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import SMA
from surmount.logging import log

class TradingStrategy(Strategy):
    @property
    def assets(self):
        return ["AAPL"]

    @property
    def interval(self):
        return "1day"  # Daily interval for checking SMA crossovers

    def run(self, data):
        # Initialize the allocation dictionary with no allocation
        allocation_dict = {"AAPL": 0}

        # Extract the close prices data for AAPL
        close_prices = [i["AAPL"]["close"] for i in data["ohlcv"]]

        # Calculate 7-day and 21-day Simple Moving Averages (SMA)
        sma_short = SMA("AAPL", data["ohlcv"], 7)
        sma_long = SMA("AAPL", data["ohlcv"], 21)

        # Ensure we have enough data points for both SMAs to be valid
        if len(sma_short) > 0 and len(sma_long) > 0:
            # Check for the crossover conditions
            if sma_short[-1] > sma_long[-1] and sma_short[-2] < sma_long[-2]:
                # This condition checks if the SMA7 crosses above SMA21 - indicating a buy signal
                log("SMA7 has crossed above SMA21. Buying signal.")
                allocation_dict["AAPL"] = 1  # Allocate 100% to AAPL
            elif sma_short[-1] < sma_long[-1] and sma_short[-2] > sma_long[-2]:
                # This condition checks if the SMA7 crosses below SMA21 - indicating a sell signal
                log("SMA7 has crossed below SMA21. Selling signal.")
                allocation_dict["AAPL"] = 0  # No allocation to AAPL

        return TargetAllocation(allocation_dict)