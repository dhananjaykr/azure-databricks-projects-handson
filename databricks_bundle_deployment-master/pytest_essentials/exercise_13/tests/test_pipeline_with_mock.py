from unittest.mock import patch

from order_pipeline.pipeline import run_pipeline


@patch("order_pipeline.pipeline.get_orders")
def test_pipeline_with_mock(mock_get_orders):
    mock_get_orders.return_value = [
        {"id": 10, "amount": 500},
        {"id": 20, "amount": -100},
    ]

    result = run_pipeline()

    assert result == [
        {"id": 10, "amount": 500},
    ]
