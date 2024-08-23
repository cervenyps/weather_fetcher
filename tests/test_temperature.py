import unittest
from weather_fetcher.temperature import get_temperatures

class TestTemperatureFetcher(unittest.TestCase):
    def test_get_temperatures(self):
        temperatures = get_temperatures()
        self.assertIsInstance(temperatures, dict)
        for city, temp in temperatures.items():
            self.assertTrue(isinstance(temp, float) or isinstance(temp, str))

if __name__ == "__main__":
    unittest.main()
