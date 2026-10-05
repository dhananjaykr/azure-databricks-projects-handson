# Exercise 15: Test Coverage

This exercise runs pytest with coverage reporting.

## Files

```text
exercise_15/
  pytest.ini
  src/
    order_pipeline/
      __init__.py
      config.py
      extract.py
      transform.py
      pipeline.py
  tests/
    test_config.py
    test_pipeline.py
    test_transform.py
```

## Run Tests

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_15
python -m pytest -v
```

## Run Tests With Coverage

```powershell
python -m pytest --cov=order_pipeline --cov-report=term-missing -v
```

## What To Notice

Coverage shows which lines of Python code were executed by tests.

`term-missing` shows line numbers that were not covered.

Coverage does not prove that the logic is correct. It shows how much code the tests touched.
