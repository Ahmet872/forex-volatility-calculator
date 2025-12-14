# MT5 Volatility Analyzer

This project is a small, focused volatility analysis tool built on top of MetaTrader 5 price data.

It connects to an MT5 terminal, retrieves recent candle data for selected Forex symbols, calculates basic volatility metrics, and outputs the results in a clean, machine-readable format.

The goal of this project is not to provide a trading strategy, but to **demonstrate how volatility can be measured and interpreted using real market data**.

---

## Project Scope

This tool intentionally keeps its scope limited:

* No graphical interface
* No trading logic
* No signal generation
* No real-time tick processing

Instead, it focuses on doing one thing well:
**measuring price volatility in a transparent and reproducible way**.

This makes the project suitable as:

* A learning reference
* A preprocessing module for larger systems
* A lightweight volatility inspection tool

---

## What Is Volatility?

Volatility describes how much a price fluctuates over time.

* Higher volatility means larger and less predictable price movements
* Lower volatility means smoother and more stable price behavior

Volatility does **not** indicate market direction.
It only reflects the **magnitude and variability of price movement**.

---

## Volatility Metrics Used

The project calculates two complementary metrics.

---

### Average True Range (ATR)

ATR measures the **average price movement per candle** over a given period.

* Based on high, low, and close prices
* Expressed in raw price units
* Directly affected by the instrument’s price scale

Example interpretation:

* ATR ≈ 0.00010 on EURUSD corresponds to roughly 1 pip per candle
* ATR ≈ 0.02 on USDJPY corresponds to roughly 2 pips per candle

ATR is commonly used for:

* Risk management
* Stop-loss and take-profit sizing
* Evaluating short-term price activity

---

### Volatility (Historical / Realized)

This metric represents the **statistical dispersion of recent price returns**.

* Calculated from logarithmic returns
* Normalized and scale-independent.
* Suitable for comparing different symbols.

Higher values indicate;

* More irregular price behavior.
* Increased uncertainty.

Lower values indicate:

* More stable price movement.
* Tighter and more predictable ranges.

This metric is useful for:

* Market rejime detection.
* Symbol comparison.
* Strategy filtering.

---

## Candle-Based Calculation Model

All calculations in this project are **candle-based**.

* Values update only after a candle has closed.
* Metrics remain constant while a candle is still forming.
* This avoids repainting and unstable intermediate values.

The update frequency depends on the selected timeframe:

* M1 updates every minute.
* H1 updates every hour,
* D1 updatess daily.

This behavior is intentional and reflects standard trading system design.

---

## Example Output

```json
[
  {
    "symbol": "EURUSD",
    "atr": 0.00011,
    "volatility": 0.00008
  },
  {
    "symbol": "USDJPY",
    "atr": 0.02157,
    "volatility": 0.00009
  }
]
```

How to read this output:

* ATR show absolute price movement per candle.
* Volatility shows normalized price variability.
* Both metrics together provide a clearer picture of market behavior.

---

## What This Project Is Not

This project does not attempt to:

* Predict market direction.
* React to news events.
* Measure tick-level microstructure volatility.

Those concerns are intentionally left out to keep the design simple and robust.

---

## Intended Audience

This project is designed for:

* Developers exploring market data analysis.
* Traders interested in understanding volatility metrics.
* Engineers looking for a clean MT5-based data example.

It aims to be **educational without being simplistic**, and **practical without being overengineered**.

## License
MIT License