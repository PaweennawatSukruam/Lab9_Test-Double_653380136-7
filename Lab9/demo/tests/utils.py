from io import BytesIO
from requests.models import Response


def get_mock_country_api_response():
    """
    Method to create sample response from the API (e.g. example-country.com/name)
    """
    mock_api_response = Response()
    mock_api_response.status_code = 200

    mock_api_response.raw = BytesIO(b'{ "data" : ["Thailand", "England", "Taiwan", '
                                    b'"Tunisia", "Indonesia", "America", "Japan"]}')

    return mock_api_response


# example = get_mock_country_api_response().json()
# print(type(example), example)

