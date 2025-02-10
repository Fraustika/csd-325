import unittest
from city_functions import format_city_country

class TestCityFunctions(unittest.TestCase):
    def test_city_country(self):
        """Test that the function returns the correct string."""
        # Test case for city and country only
        result = format_city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")

        # Test case for city and country only
        result = format_city_country("New York", "USA")
        self.assertEqual(result, "New York, USA")

        # Test case for city and country only
        result = format_city_country("Tokyo", "Japan")
        self.assertEqual(result, "Tokyo, Japan")

# Run the tests
if __name__ == '__main__':
    unittest.main()