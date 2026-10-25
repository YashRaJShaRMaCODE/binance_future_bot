import re
from decimal import Decimal, InvalidOperation

MAX_DECIMAL_TEXT_LENGTH = 64


def positive_decimal(value, label):
    value_text = str(value)
    if len(value_text) > MAX_DECIMAL_TEXT_LENGTH:
        raise ValueError(f"{label} must fit within {MAX_DECIMAL_TEXT_LENGTH} characters")
    try:
        number = Decimal(value_text)
    except (InvalidOperation, ValueError):
        raise ValueError(f"{label} must be a positive decimal") from None
    if not number.is_finite() or number <= 0:
        raise ValueError(f"{label} must be a positive decimal")
    decimal = number.as_tuple()
    integer_digits = max(1, len(decimal.digits) + decimal.exponent)
    fractional_digits = max(0, -decimal.exponent)
    formatted_length = integer_digits + fractional_digits + bool(fractional_digits)
    if formatted_length > MAX_DECIMAL_TEXT_LENGTH:
        raise ValueError(f"{label} must fit within {MAX_DECIMAL_TEXT_LENGTH} characters")
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
