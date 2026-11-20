import json
import tempfile
import unittest
from pathlib import Path

from collect_google_trends import ConfigError, load_config


class ConfigValidationTests(unittest.TestCase):
    def write_config(self, payload):
        temp = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=".json", delete=False)
        with temp:
            json.dump(payload, temp)
        self.addCleanup(Path(temp.name).unlink, missing_ok=True)
        return Path(temp.name)

    def valid_config(self):
        return {
            "project_slug": "guardian",
            "geo": "BR",
            "timeframe": "today 12-m",
            "keywords": ["portaria remota", "monitoramento de alarme"],
            "include_trending_now": False,
        }

    def test_accepts_valid_config(self):
        config = load_config(self.write_config(self.valid_config()))
        self.assertEqual(config["project_slug"], "guardian")
        self.assertEqual(config["geo"], "BR")
        self.assertEqual(len(config["keywords"]), 2)

    def test_rejects_more_than_five_keywords(self):
        payload = self.valid_config()
        payload["keywords"] = [f"termo {i}" for i in range(6)]
        with self.assertRaises(ConfigError):
            load_config(self.write_config(payload))

    def test_rejects_commas_inside_keyword(self):
        payload = self.valid_config()
        payload["keywords"] = ["alarme, monitoramento"]
        with self.assertRaises(ConfigError):
            load_config(self.write_config(payload))

    def test_rejects_duplicate_keywords(self):
        payload = self.valid_config()
        payload["keywords"] = ["Portaria Remota", "portaria remota"]
        with self.assertRaises(ConfigError):
            load_config(self.write_config(payload))

    def test_rejects_invalid_project_slug(self):
        payload = self.valid_config()
        payload["project_slug"] = "../guardian"
        with self.assertRaises(ConfigError):
            load_config(self.write_config(payload))

    def test_rejects_invalid_timeframe(self):
        payload = self.valid_config()
        payload["timeframe"] = "last year && curl evil"
        with self.assertRaises(ConfigError):
            load_config(self.write_config(payload))


if __name__ == "__main__":
    unittest.main()
