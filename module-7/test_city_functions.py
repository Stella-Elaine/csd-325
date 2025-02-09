

import unittest
from city_functions import format_city_country

class CityCountryTestCase(unittest.TestCase):
    "Tests for the 'format_city_country' function."

    def test_city_country(self):
        "Does 'Santiago, Chile' work correctly?"
        formatted_name = format_city_country("santiago", "chile")
        self.assertEqual(formatted_name, "Santiago, Chile")

if __name__ == "__main__":
    unittest.main()
