from unittest.mock import patch
from utils import get_mock_currency_api_response
from currency_exchanger import CurrencyExchanger
import unittest

class TestCurrencyExchanger(unittest.TestCase):
    def setUp(self):
        self.currency_exchanger = CurrencyExchanger()
        self.mock_api_response = get_mock_currency_api_response()
        self.base_currency="THB"
        self.target_currency="KRW"

    @patch("currency_exchanger.requests")
    def test_get_currency_rate(self,mock_request):
        mock_request.get.return_value = self.mock_api_response
        self.currency_exchanger.get_currency_rate()
        mock_request.get.assert_called_once()
        mock_request.get.assert_called_with('https://coc-kku-bank.com/foreign-exchange',  params={'from': 'THB', 'to': 'KRW'})
        self.assertIsNotNone(self.currency_exchanger.api_response)
        self.assertEqual(self.currency_exchanger.api_response, self.mock_api_response.json())

    @patch("currency_exchanger.requests")
    def test_currency_exchange(self,mock_request):
        mock_request.get.return_value = self.mock_api_response
        result = self.currency_exchanger.currency_exchange(1)
        mock_request.get.assert_called_once()
        mock_request.get.assert_called_with('https://coc-kku-bank.com/foreign-exchange',  params={'from': 'THB', 'to': 'KRW'})
        expected_result = 38.69
        self.assertEqual(result,expected_result)
        




if __name__ == '__main__':
    unittest.main()