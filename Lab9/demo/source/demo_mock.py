from datetime import datetime
from unittest.mock import Mock


def is_today_even(today_date):
    # Extract the day of the month
    day_of_month = today_date.day

    # Check if the day is odd
    if day_of_month % 2 == 0:
        return True
    else:
        return False


# save an odd date
odd_date = datetime(year=2024, month=8, day=19)

datetime = Mock()

datetime.today.return_value = odd_date

# Get today's date
today = datetime.today()

assert is_today_even(today)
