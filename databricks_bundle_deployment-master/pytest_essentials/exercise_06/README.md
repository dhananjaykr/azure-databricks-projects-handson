# Exercise 06: Fixtures

This exercise uses a fixture as reusable test setup.

## Files

```text
exercise_06/
  pytest.ini
  tests/
    conftest.py
    test_orders.py
```

## Run

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_06
python -m pytest -v
```

## What To Notice

The `sample_orders` fixture is defined once.

Multiple tests receive the same setup by asking for `sample_orders` as a function argument.

Fixtures are useful for sample input data, config, job parameters, Spark sessions, temporary files, and mock clients.
