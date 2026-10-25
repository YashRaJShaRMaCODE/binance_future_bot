import argparse

from order_validation import build_limit_order


def place_limit_order(symbol, side, quantity, price, client=None):
    payload = build_limit_order(symbol, side, quantity, price)
    if client is None:
        from utils import get_binance_client
        client = get_binance_client()
    return client.futures_create_order(**payload)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Preview a Binance USDⓈ-M Futures testnet limit order.")
    parser.add_argument("symbol")
    parser.add_argument("side", choices=("BUY", "SELL"))
    parser.add_argument("quantity")
    parser.add_argument("price")
    parser.add_argument("--submit-testnet", action="store_true", help="place this order on Binance Futures Testnet")
    args = parser.parse_args(argv)
    try:
        order = build_limit_order(args.symbol, args.side, args.quantity, args.price)
        if not args.submit_testnet:
            print(f"Preview only: {order}. Add --submit-testnet to place it on Binance Futures Testnet.")
            return 0
        from logger import logger
        result = place_limit_order(**{k: order[k] for k in ("symbol", "side", "quantity", "price")})
        logger.info("Testnet limit order accepted: %s %s %s @ %s, status=%s, order_id=%s",
                    order["symbol"], order["side"], order["quantity"], order["price"],
                    result.get("status"), result.get("orderId"))
        print({key: result.get(key) for key in ("symbol", "side", "type", "origQty", "price", "status", "orderId")})
        return 0
    except Exception as e:
        if args.submit_testnet:
            from logger import logger
            logger.error("Limit order failed: %s", type(e).__name__)
        print(f"Order failed: {type(e).__name__}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
