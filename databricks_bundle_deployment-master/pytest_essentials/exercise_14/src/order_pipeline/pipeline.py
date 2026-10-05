from order_pipeline.extract import get_orders
from order_pipeline.transform import clean_orders


def run_pipeline():
    orders = get_orders()
    return clean_orders(orders)
