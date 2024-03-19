import unittest
import requests


class AppReachableTest(unittest.TestCase):

    def test_connection(self):
        weatherapp_add = "http://34.230.48.168/"
        response = requests.get(weatherapp_add, timeout=10).status_code
        self.assertEqual(response, 200, "Web app is not reachable")


if __name__ == "main":
    unittest.main()
