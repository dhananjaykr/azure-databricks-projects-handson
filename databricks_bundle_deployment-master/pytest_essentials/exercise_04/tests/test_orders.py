import pytest

from orders import calculate_discount


@pytest.mark.parametrize(
    "amount,expected",
    [
        (1000, 0),
        (5000, 250),
        (10000, 1000),
        (20000, 2000),
    ],
)
def test_calculate_discount(amount, expected):
    assert calculate_discount(amount) == expected
