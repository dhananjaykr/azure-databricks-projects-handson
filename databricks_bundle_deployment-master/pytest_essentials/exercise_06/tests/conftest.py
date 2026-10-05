import pytest


@pytest.fixture
def sample_orders():
    return [
        {"order_id": 1, "amount": 100},
        {"order_id": 2, "amount": 200},
        {"order_id": 3, "amount": 300},
    ]
