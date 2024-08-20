# Lab9 - Test double
# Integration testing using Mock - Crate Mock object to mimic the behavior of external service

from unittest.mock import patch
import sys
sys.path.insert(0,'/workspaces/Lab9_Test-Double_653380136-7/Lab9/demo/source')
sys.path.insert(0,'/workspaces/Lab9_Test-Double_653380136-7/Lab9/demo/tests')
from country import Country
from utils import get_mock_country_api_response
# from demo.source.country import Country
# from demo.tests.utils import get_mock_country_api_response

import unittest


class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country()
        self.mock_api_response = get_mock_country_api_response()

    # Mock the 'request' package from source.country
    @patch("country.requests")
    def test_get_country_name(self, mock_request):
        # Assign mock's return value
        mock_request.get.return_value = self.mock_api_response

        # Act - execute class under test
        self.country.get_country_name()

        # Check whether the mocked method is called
        mock_request.get.assert_called_once()

        # Check whether the mocked method is called with the right parameter
        mock_request.get.assert_called_with("https://example-country.com/name")

        # Assert the returned responses
        self.assertIsNotNone(self.country.country_name_response)
        self.assertEqual(self.country.country_name_response, self.mock_api_response.json())

    @patch("country.requests")
    def test_get_country_name_start_with_letter(self, mock_request):
        mock_request.get.return_value = self.mock_api_response

        result = self.country.get_country_name_start_with_letter("t")

        mock_request.get.assert_called_once()

        mock_request.get.assert_called_with("https://example-country.com/name")

        expected_result = ["Thailand", "Taiwan", "Tunisia"]

        self.assertListEqual(result, expected_result)
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()
