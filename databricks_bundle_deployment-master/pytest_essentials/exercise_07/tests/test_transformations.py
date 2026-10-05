from transformations import clean_orders


def test_clean_orders():
    input_data = [
        {"order_id": 1, "amount": 100},
        {"order_id": 2, "amount": -50},
        {"order_id": 3, "amount": 200},
    ]

    result = clean_orders(input_data)

    assert result == [
        {"order_id": 1, "amount": 100},
        {"order_id": 3, "amount": 200},
    ]
