import pandas as pd
import numpy as np


class VolatilityCalculator:
    @staticmethod
    def calculate_atr(df: pd.DataFrame, period: int) -> float:
        # Extract OHLC componnts required for True Range calculation
        high = df["high"]
        low = df["low"]
        close = df["close"].shift(1)

        tr = pd.concat(
            [high - low,
            (high - close).abs(),
            (low - close).abs()],axis=1).max(axis=1)
                
        atr = tr.rolling(period).mean().iloc[-1]
        return float(round(atr, 5))

    @staticmethod
    def calculate_historical_volatility(
        df: pd.DataFrame,
        period: int) -> float:# Log returns stabilize variance for volatility estimation
            log_returns = np.log(df["close"] / df["close"].shift(1))
            hv = log_returns.rolling(period).std().iloc[-1]
            return float(round(hv, 6))

            