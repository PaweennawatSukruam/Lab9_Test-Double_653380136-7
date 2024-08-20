from io import BytesIO
from requests.models import Response


def get_mock_currency_api_response():
    """
    Method to create sample response from the API (e.g. coc-kku-bank.com/foreign-exchange)
    """
    mock_api_response = Response()
    mock_api_response.status_code = 200

    mock_api_response.raw = BytesIO(b'{"base": "THB", "result": {"KRW": 38.69}}')

    return mock_api_response


example = get_mock_currency_api_response().json()
print(type(example), example)

