# Binance Futures testnet CLI

A small command-line example for previewing and placing USDⓈ-M Futures market and limit orders on the Binance Futures **testnet**. The client is hard-wired to testnet; this project does not provide a mainnet trading mode.

## Setup

Use Python 3.10 or later and create a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Add Futures testnet API credentials to `.env`. Keep withdrawals disabled, never reuse mainnet credentials, and do not commit `.env` or `bot.log`.

## Preview and place testnet orders

Commands preview by default and make no API request:

```powershell
python src/market_orders.py BTCUSDT BUY 0.01
python src/limit_order.py BTCUSDT SELL 0.01 65000
```

To explicitly place a testnet order, append `--submit-testnet`:

```powershell
python src/market_orders.py BTCUSDT BUY 0.01 --submit-testnet
python src/limit_order.py BTCUSDT SELL 0.01 65000 --submit-testnet
```

The exchange remains responsible for symbol-specific quantity and price filters. Start with small testnet orders and check the returned status. A limit order can remain open until it fills or is cancelled in the Binance testnet interface.

## Checks

```powershell
python -m unittest discover -s tests
python -m compileall -q src tests
```

Only market and limit order entry points are implemented. TWAP, stop-limit, grid, and OCO features from earlier drafts are not included.
