from order_pipeline.pipeline import run_pipeline


def test_run_pipeline():
    result = run_pipeline("dev")

    assert result["catalog"] == "dev_catalog"
    assert result["row_count"] == 2
    assert result["total_amount"] == 400
    assert result["rows"] == [
        {"id": 1, "amount": 100},
        {"id": 3, "amount": 300},
    ]
