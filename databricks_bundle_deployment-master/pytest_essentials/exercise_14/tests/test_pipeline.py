import pytest

from order_pipeline.pipeline import run_pipeline


@pytest.mark.integration
def test_pipeline():
    result = run_pipeline()

    assert result == [
        {"id": 1, "amount": 100},
        {"id": 3, "amount": 300},
    ]
