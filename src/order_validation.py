import re
from decimal import Decimal, InvalidOperation


def positive_decimal(value, label):
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError(f"{label} must be a positive decimal") from None
    if not number.is_finite() or number <= 0:
        raise ValueError(f"{label} must be a positive decimal")
    return format(number, "f")


def validate_order(symbol, side, quantity, price=None):
    symbol = str(symbol).strip().upper()
    side = str(side).strip().upper()
    if not re.fullmatch(r"[A-Z0-9]{2,20}", symbol):
        raise ValueError("Symbol must contain 2 to 20 letters or digits")
    if side not in {"BUY", "SELL"}:
        raise ValueError("Side must be BUY or SELL")

    order = {"symbol": symbol, "side": side, "quantity": positive_decimal(quantity, "Quantity")}
    if price is not None:
        order["price"] = positive_decimal(price, "Price")
    return order


def build_market_order(symbol, side, quantity):
    return {**validate_order(symbol, side, quantity), "type": "MARKET"}


def build_limit_order(symbol, side, quantity, price):
    return {**validate_order(symbol, side, quantity, price), "type": "LIMIT", "timeInForce": "GTC"}
