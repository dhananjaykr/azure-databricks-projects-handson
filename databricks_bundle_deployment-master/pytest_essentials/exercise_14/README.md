# Exercise 14: Unit And Integration Markers

This exercise separates unit tests and integration-style tests with pytest markers.

## Files

```text
exercise_14/
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

## Run All Tests

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_14
python -m pytest -v
```

## Run Unit Tests Only

```powershell
python -m pytest -m unit -v
```

## Run Integration Tests Only

```powershell
python -m pytest -m integration -v
```

## What To Notice

Markers let you choose which group of tests to run.

This becomes useful when the deployment flow has separate stages for unit tests, bundle validation, deployment, and integration tests.
