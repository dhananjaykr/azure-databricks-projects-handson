def clean_orders(orders):
    return [
        order
        for order in orders
        if order["amount"] > 0
    ]
