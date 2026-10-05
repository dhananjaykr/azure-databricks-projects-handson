# Exercise 13: Mock The Extraction Layer

This exercise tests the pipeline while replacing the extraction step with a mock.

## Files

```text
exercise_13/
  pytest.ini
  src/
    order_pipeline/
      __init__.py
      extract.py
      transform.py
      pipeline.py
  tests/
    test_pipeline_with_mock.py
```

## Run

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_13
python -m pytest -v
```

## What To Notice

The test patches `order_pipeline.pipeline.get_orders`.

The real extractor is not used in this test.

The pipeline still runs the real transformation logic.

This pattern is useful when a source is slow, costly, unavailable, or outside the unit test boundary.
