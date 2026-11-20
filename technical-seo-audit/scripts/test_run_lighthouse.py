import json
import tempfile
import unittest
from pathlib import Path

from run_lighthouse import ConfigError, load_config, validate_public_url


class LighthouseConfigTests(unittest.TestCase):
    def write_config(self, payload):
        temp = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".json", delete=False)
        with temp:
            json.dump(payload, temp)
        self.addCleanup(Path(temp.name).unlink, missing_ok=True)
        return Path(temp.name)

    def valid(self):
        return {
            "project_slug": "guardian",
            "urls": ["https://guardianseg.com.br/"],
            "preset": "mobile",
        }

    def test_accepts_valid_config(self):
        config = load_config(self.write_config(self.valid()))
        self.assertEqual(config["project_slug"], "guardian")
        self.assertEqual(config["preset"], "mobile")
        self.assertEqual(config["urls"], ["https://guardianseg.com.br/"])

    def test_normalizes_missing_path(self):
        self.assertEqual(validate_public_url("https://example.com"), "https://example.com/")

    def test_rejects_http(self):
        with self.assertRaises(ConfigError):
            validate_public_url("http://example.com")

    def test_rejects_localhost(self):
        with self.assertRaises(ConfigError):
            validate_public_url("https://localhost")

    def test_rejects_private_ip(self):
        with self.assertRaises(ConfigError):
            validate_public_url("https://192.168.1.10")

    def test_rejects_url_credentials(self):
        with self.assertRaises(ConfigError):
            validate_public_url("https://user:pass@example.com")

    def test_rejects_query_string(self):
        with self.assertRaises(ConfigError):
            validate_public_url("https://example.com/?token=abc")

    def test_rejects_more_than_five_urls(self):
        payload = self.valid()
        payload["urls"] = [f"https://example{i}.com/" for i in range(6)]
        with self.assertRaises(ConfigError):
            load_config(self.write_config(payload))

    def test_rejects_invalid_slug(self):
        payload = self.valid()
        payload["project_slug"] = "../guardian"
        with self.assertRaises(ConfigError):
            load_config(self.write_config(payload))

    def test_rejects_invalid_preset(self):
        payload = self.valid()
        payload["preset"] = "tablet"
        with self.assertRaises(ConfigError):
            load_config(self.write_config(payload))


if __name__ == "__main__":
    unittest.main()
