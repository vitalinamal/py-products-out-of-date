import pytest

from datetime import date
from unittest.mock import patch
from app.main import outdated_products


@pytest.mark.parametrize(
    "user_input, new_date, expected_output",
    [
        (  # Start of the first parameter set
            [  # user_input: list of product dictionaries
                {
                    "name": "salmon",
                    "expiration_date": date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": date(2022, 2, 1),
                    "price": 160
                }
            ],
            date(2022, 2, 2),  # new_date: the fixed current date for the test
            ["duck"]  # expected_output: expected result from the function
        )  # End of the first parameter set
        # Additional parameter sets can be added here as tuples.
    ]
)
def test_outdated_products(
        user_input: list,
        new_date: object,
        expected_output: list
) -> None:
    with patch("app.main.datetime.date.today", return_value=new_date):
        assert outdated_products(user_input) == expected_output
