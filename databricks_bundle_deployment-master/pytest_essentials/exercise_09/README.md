# Exercise 09: Configuration Tests

This exercise tests environment-based configuration.

## Files

```text
exercise_09/
  config.py
  pytest.ini
  tests/
    test_config.py
```

## Run

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_09
python -m pytest -v
```

## What To Notice

Each environment maps to a catalog name.

This maps to Databricks Bundle targets such as `dev`, `test`, and `prod`.
