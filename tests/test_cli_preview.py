import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PreviewCommandTests(unittest.TestCase):
    def run_preview(self, script, *args):
        env = {key: value for key, value in os.environ.items()
               if key not in {"BINANCE_API_KEY", "BINANCE_API_SECRET"}}
        with tempfile.TemporaryDirectory(dir=ROOT) as temp_dir:
            result = subprocess.run(
                [sys.executable, "-S", str(ROOT / "src" / script), *args],
                cwd=temp_dir,
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertFalse(Path(temp_dir, "bot.log").exists())
            return result

    def test_market_preview_needs_no_exchange_package_or_credentials(self):
        result = self.run_preview("market_orders.py", "BTCUSDT", "BUY", "0.01")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Preview only", result.stdout)
        self.assertIn("MARKET", result.stdout)

    def test_limit_preview_needs_no_exchange_package_or_credentials(self):
        result = self.run_preview("limit_order.py", "BTCUSDT", "SELL", "0.01", "65000")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Preview only", result.stdout)
        self.assertIn("LIMIT", result.stdout)


if __name__ == "__main__":
    unittest.main()
