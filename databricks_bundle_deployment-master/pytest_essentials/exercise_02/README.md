# Exercise 02: Reading A Pytest Failure

This exercise shows how pytest explains a failing test.

The normal test suite passes. A separate demo file contains an intentional failure.

## Files

```text
exercise_02/
  calculator.py
  pytest.ini
  tests/
    test_calculator.py
  demos/
    test_intentional_failure.py
```

## Run The Passing Tests

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_02
python -m pytest -v
```

## Run The Failing Demo

```powershell
python -m pytest demos/test_intentional_failure.py -v
```

## What To Notice

Read the failure message carefully.

Pytest shows the expected value, the actual value, and the exact assertion that failed.

In a deployment flow, a failing test should stop the next step.
