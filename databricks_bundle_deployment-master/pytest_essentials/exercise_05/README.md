# Exercise 05: Exception Tests

This exercise tests both valid input and invalid input.

## Files

```text
exercise_05/
  orders.py
  pytest.ini
  tests/
    test_orders.py
```

## Run

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_05
python -m pytest -v
```

## What To Notice

`pytest.raises` checks that the expected exception is raised.

The `match` argument checks the error message.

This is useful for invalid configuration, missing parameters, bad input, and invalid file paths.
