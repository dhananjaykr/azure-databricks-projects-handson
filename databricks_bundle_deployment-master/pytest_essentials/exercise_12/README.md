# Exercise 12: Small Pipeline Tests

This exercise tests a small extract-transform pipeline.

## Files

```text
exercise_12/
  pytest.ini
  src/
    order_pipeline/
      __init__.py
      extract.py
      transform.py
      pipeline.py
  tests/
    test_transform.py
    test_pipeline.py
```

## Run

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_12
python -m pytest -v
```

## What To Notice

`extract.py` gets input data.

`transform.py` cleans the data.

`pipeline.py` connects the steps.

The tests check the transformation and the full pipeline result.
