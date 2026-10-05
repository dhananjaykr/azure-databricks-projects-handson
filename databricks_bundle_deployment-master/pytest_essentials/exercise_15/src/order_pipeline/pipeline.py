from order_pipeline.config import get_catalog
from order_pipeline.extract import get_orders
from order_pipeline.transform import clean_orders, total_amount


def run_pipeline(environment):
    catalog = get_catalog(environment)
    orders = get_orders()
    clean_data = clean_orders(orders)

    return {
        "catalog": catalog,
        "row_count": len(clean_data),
        "total_amount": total_amount(clean_data),
        "rows": clean_data,
    }
