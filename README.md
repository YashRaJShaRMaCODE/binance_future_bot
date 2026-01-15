Binance Futures Trading Bot (CLI-Based)
📌 Overview

This project is a CLI-based trading bot built in Python for interacting with Binance USDT-M Futures.
It supports core and advanced order types with robust input validation, structured logging, and a modular architecture.

The bot is designed for Binance Futures Testnet to ensure safe testing without real funds.

🚀 Features
✅ Core Orders (Mandatory)

Market Orders (BUY / SELL)

Limit Orders

⭐ Advanced Orders (Bonus)

Stop-Limit Orders

TWAP (Time-Weighted Average Price) strategy

OCO (One-Cancels-the-Other) (planned / optional)

Grid Trading Strategy (optional)

🔐 Reliability & Safety

Input validation (symbol, quantity, price)

Centralized structured logging

Secure API key handling via environment variables

No hardcoded credentials

🧱 Project Structure
binance_futures_bot/
│
├── src/
│   ├── market_orders.py      # Market order logic
│   ├── limit_orders.py       # Limit order logic
│   ├── utils.py              # Binance client & helpers
│   ├── logger.py             # Logging configuration
│   └── advanced/
│       ├── stop_limit.py
│       ├── twap.py
│       └── oco.py
│
├── bot.log                   # Structured logs
├── README.md                 # Documentation
├── report.pdf                # Analysis & screenshots
└── .env                      # API credentials (not committed)

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-url>
cd binance_futures_bot

2️⃣ Create Virtual Environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3️⃣ Install Dependencies
pip install python-binance python-dotenv

4️⃣ Configure Environment Variables

Create a .env file in the project root:

BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here


⚠️ Important

Use Binance Futures Testnet API keys

Never commit .env to GitHub

🔌 Binance Testnet Configuration

This project uses Binance Futures Testnet for safe testing.

Testnet URL is handled internally via testnet=True

No real money is involved

No Aadhaar / PAN required for testnet usage

▶️ Usage
🔹 Market Order
python src/market_orders.py BTCUSDT BUY 0.01

🔹 Limit Order
python src/limit_orders.py BTCUSDT SELL 0.01 65000

🔹 Stop-Limit Order
python src/advanced/stop_limit.py BTCUSDT BUY 0.01 64000 64500

🔹 TWAP Strategy
python src/advanced/twap.py BTCUSDT BUY 0.05 5 30


(splits quantity into 5 orders over 30-second intervals)

📝 Logging

All actions are logged in bot.log with timestamps:

2026-01-16 12:45:02 | INFO | Market order placed: BTCUSDT BUY 0.01
2026-01-16 12:45:04 | ERROR | Invalid quantity provided


Logs include:

Order requests

API responses

Validation errors

Execution status

🛡️ Security Best Practices

API keys stored securely using .env

Withdrawals permission disabled

No credentials hardcoded

API keys not exposed in logs or repository

📄 Report

The report.pdf includes:

CLI execution screenshots

Explanation of implemented order types

Logging demonstration

Challenges faced

Future improvements

🔮 Future Enhancements

Full OCO order support

Grid trading automation

Strategy backtesting using historical data

Configurable risk management

👤 Author

Yash Raj Sharma
GitHub: YashRaJShaRMaCODE