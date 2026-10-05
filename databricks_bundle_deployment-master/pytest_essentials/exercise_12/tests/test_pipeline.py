from order_pipeline.pipeline import run_pipeline


def test_pipeline():
    result = run_pipeline()

    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3
