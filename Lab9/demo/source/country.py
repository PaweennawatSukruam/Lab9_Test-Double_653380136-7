# Lab9 - Test double
# Simple interation between class (e.g. Country) and external service (e.g. country information API)

import requests


class Country:
    def __init__(self):
        self.country_name_response = None
        # Endpoint to the external service, in this case is the country information API
        self.api_url = "https://example-country.com/name"

    def get_country_name(self):
        """
        Method to get data/response from API
        """
        try:
            response = requests.get(self.api_url)
            if response.status_code in (200, 201):
                self.country_name_response = response.json()
        except requests.exceptions.RequestException:
            self.country_name_response = None

    def get_country_name_start_with_letter(self, letter="a"):
        """
        Method to query the country name starting with specific letter
        """
        self.get_country_name()
        all_country_name = self.country_name_response["data"]
        result = []
        for name in all_country_name:
            if name.lower().startswith(letter.lower()):
                result.append(name)
        return result
