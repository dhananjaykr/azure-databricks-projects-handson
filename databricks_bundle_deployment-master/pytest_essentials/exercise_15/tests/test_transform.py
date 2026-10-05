from order_pipeline.transform import clean_orders, total_amount


def test_clean_orders():
    orders = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": -50},
        {"id": 3, "amount": 300},
    ]

    assert clean_orders(orders) == [
        {"id": 1, "amount": 100},
        {"id": 3, "amount": 300},
    ]


def test_total_amount():
    orders = [
        {"id": 1, "amount": 100},
        {"id": 3, "amount": 300},
    ]

    assert total_amount(orders) == 400
