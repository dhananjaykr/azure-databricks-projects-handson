def clean_orders(orders):
    return [
        order
        for order in orders
        if order["amount"] > 0
    ]


def total_amount(orders):
    return sum(order["amount"] for order in orders)
