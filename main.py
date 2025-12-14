import json
import MetaTrader5 as mt5
from mt5_data_collector import MT5DataCollector
from volatility_calculator import VolatilityCalculator

TIMEFRAME_MAP = {
    "M1": mt5.TIMEFRAME_M1,
    "M5": mt5.TIMEFRAME_M5,
    "M15": mt5.TIMEFRAME_M15,
    "M30": mt5.TIMEFRAME_M30,
    "H1": mt5.TIMEFRAME_H1,
    "H4": mt5.TIMEFRAME_H4,
    "D1": mt5.TIMEFRAME_D1,}


def load_config(path: str) -> dict:# Load runtime configuration from JSON file
    with open(path, "r") as f:
        return json.load(f)


def main():# Read application configuration
    config = load_config("config.json")
    collector = MT5DataCollector(
        host=config["mt5"]["host"],
        port=config["mt5"]["port"],
        timeout=config["mt5"]["timeout"])
    collector.connect()
    timeframe = TIMEFRAME_MAP[config["timeframe"]]
    results = []

    for symbol in config["symbols"]:
        df = collector.get_candles(# Retrieve historical candle data for the symbol
            symbol=symbol,
            timeframe=timeframe,
            candles_count=config["candles_count"])
        
        atr = VolatilityCalculator.calculate_atr(# Calculate ATR-based volatility metric
            df,
            config["atr_period"])
        
        hv = VolatilityCalculator.calculate_historical_volatility(# Calculate log-return based historical volatility
            df,
            config["hv_period"])
        
        results.append(
            {"symbol": symbol,
             "atr": atr,
             "historical_volatility": hv})   
    collector.shutdown()# Ensure MT5 connection is properly closed

    if config["output"]["format"] == "json":
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
