import MetaTrader5 as mt5
import pandas as pd


class MT5DataCollector:
    def __init__(self, host: str, port: int, timeout: int):
        self.host = host
        self.port = port
        self.timeout = timeout

    def connect(self) -> None: # Initialize connection with the local MetaTrader 5 terminal
        if not mt5.initialize():
            raise RuntimeError("MT5 initialization failed")

    def shutdown(self) -> None:# Properly close MT5 connection and release resources
        mt5.shutdown()

    def get_candles(# Fetch OHLCV candle data starting from the most recent bar
        self,
        symbol: str,
        timeframe: int,
        candles_count: int) -> pd.DataFrame:
    
        rates = mt5.copy_rates_from_pos(
            symbol,
            timeframe,
            0,
            candles_count)
        

        if rates is None or len(rates) == 0:# Fail fast if MT5 returns no data
            raise ValueError(f"No data returned for {symbol}")

        df = pd.DataFrame(rates)
        df["time"] = pd.to_datetime(df["time"], unit="s")# Convert innto a pandas DataFrame
        return df
