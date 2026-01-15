from utils import get_binance_client
from logger import logger

if __name__ == "__main__":
    try:
        client = get_binance_client()
        client.futures_account()
        logger.info("Connected to Binance Futures Testnet via API")
        print("✅ Connection successful (API Testnet)")
    except Exception as e:
        logger.error(str(e))
        print("❌ Connection failed:", e)
