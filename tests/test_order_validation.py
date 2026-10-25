import unittest

from src.order_validation import build_limit_order, build_market_order, validate_order


class OrderValidationTests(unittest.TestCase):
    def test_normalizes_symbol_side_and_decimal(self):
        self.assertEqual(
            validate_order(" btcusdt ", "buy", "1e-3", "65000.00"),
            {"symbol": "BTCUSDT", "side": "BUY", "quantity": "0.001", "price": "65000.00"},
        )

    def test_market_and_limit_order_payloads(self):
        self.assertEqual(
            build_market_order("btcusdt", "buy", "0.01"),
            {"symbol": "BTCUSDT", "side": "BUY", "quantity": "0.01", "type": "MARKET"},
        )
        self.assertEqual(
            build_limit_order("BTCUSDT", "SELL", "0.01", "65000"),
            {"symbol": "BTCUSDT", "side": "SELL", "quantity": "0.01", "price": "65000",
             "type": "LIMIT", "timeInForce": "GTC"},
        )

    def test_rejects_invalid_symbol_or_side(self):
        for symbol, side in [("BTC/USDT", "BUY"), ("BTCUSDT", "SELLSHORT")]:
            with self.subTest(symbol=symbol, side=side), self.assertRaises(ValueError):
                validate_order(symbol, side, "1")

    def test_rejects_non_positive_or_non_finite_amounts(self):
        for quantity in ("0", "-1", "NaN", "Infinity", "not-a-number"):
            with self.subTest(quantity=quantity), self.assertRaises(ValueError):
                validate_order("BTCUSDT", "BUY", quantity)

    def test_rejects_decimal_exponents_that_would_expand_huge_strings(self):
        for quantity in ("1e1000000000", "1e-1000000000"):
            with self.subTest(quantity=quantity), self.assertRaisesRegex(ValueError, "64 characters"):
                validate_order("BTCUSDT", "BUY", quantity)

    def test_limit_order_requires_a_positive_price(self):
        for price in ("0", "-1", "NaN"):
            with self.subTest(price=price), self.assertRaises(ValueError):
                validate_order("BTCUSDT", "SELL", "0.1", price)


if __name__ == "__main__":
    unittest.main()
