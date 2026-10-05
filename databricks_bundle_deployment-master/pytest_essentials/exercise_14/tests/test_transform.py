import pytest

from order_pipeline.transform import clean_orders


@pytest.mark.unit
def test_clean_orders():
    orders = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": -50},
    ]

    assert clean_orders(orders) == [
        {"id": 1, "amount": 100},
    ]
