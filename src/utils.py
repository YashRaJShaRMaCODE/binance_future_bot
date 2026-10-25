import os
from binance.client import Client
from dotenv import load_dotenv
from order_validation import validate_order

load_dotenv()

def get_binance_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise RuntimeError("Set BINANCE_API_KEY and BINANCE_API_SECRET in .env")

    # ✅ THIS IS THE IMPORTANT PART
    client = Client(
        api_key,
        api_secret,
        testnet=True
    )

    return client
