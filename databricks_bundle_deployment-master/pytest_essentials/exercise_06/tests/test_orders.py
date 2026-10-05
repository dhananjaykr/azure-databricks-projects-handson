def test_order_count(sample_orders):
    assert len(sample_orders) == 3


def test_total_amount(sample_orders):
    total = sum(order["amount"] for order in sample_orders)

    assert total == 600
