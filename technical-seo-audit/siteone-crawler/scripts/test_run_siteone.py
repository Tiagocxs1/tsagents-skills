import json
import tempfile
import unittest
from pathlib import Path

from run_siteone import ConfigError, build_command, load_config, validate_public_url


class SiteOneConfigTests(unittest.TestCase):
    def write_config(self, payload):
        temp = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".json", delete=False)
        with temp:
            json.dump(payload, temp)
        self.addCleanup(Path(temp.name).unlink, missing_ok=True)
        return Path(temp.name)

    def valid(self):
        return {
            "project_slug": "guardian",
            "start_url": "https://guardianseg.com.br/",
            "device": "mobile",
        }

    def test_accepts_valid_config(self):
        cfg = load_config(self.write_config(self.valid()))
        self.assertEqual(cfg["project_slug"], "guardian")
        self.assertEqual(cfg["device"], "mobile")
        self.assertEqual(cfg["max_visited_urls"], 300)

    def test_normalizes_url(self):
        self.assertEqual(validate_public_url("https://Example.com"), "https://example.com/")

    def test_rejects_http(self):
        with self.assertRaises(ConfigError):
            validate_public_url("http://example.com")

    def test_rejects_localhost(self):
        with self.assertRaises(ConfigError):
            validate_public_url("https://localhost")

    def test_rejects_private_ip(self):
        with self.assertRaises(ConfigError):
            validate_public_url("https://10.0.0.1")

    def test_rejects_url_credentials(self):
        with self.assertRaises(ConfigError):
            validate_public_url("https://user:pass@example.com")

    def test_rejects_query_string(self):
        with self.assertRaises(ConfigError):
            validate_public_url("https://example.com/?token=abc")

    def test_rejects_too_high_rate(self):
        cfg = self.valid()
        cfg["max_requests_per_second"] = 20
        with self.assertRaises(ConfigError):
            load_config(self.write_config(cfg))

    def test_rejects_unbounded_url_limit(self):
        cfg = self.valid()
        cfg["max_visited_urls"] = 5000
        with self.assertRaises(ConfigError):
            load_config(self.write_config(cfg))

    def test_builds_low_rate_command(self):
        cfg = load_config(self.write_config(self.valid()))
        with tempfile.TemporaryDirectory() as temp:
            command = build_command(Path("/tmp/siteone-crawler"), cfg, Path(temp))
        self.assertIn("--workers=2", command)
        self.assertIn("--max-reqs-per-sec=2.0", command)
        self.assertIn("--max-visited-urls=300", command)
        self.assertFalse(any("ignore-robots" in arg for arg in command))


if __name__ == "__main__":
    unittest.main()
