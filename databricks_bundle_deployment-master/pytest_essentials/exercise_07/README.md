# Exercise 07: Transformation Tests

This exercise tests a reusable transformation function.

## Files

```text
exercise_07/
  transformations.py
  pytest.ini
  tests/
    test_transformations.py
```

## Run

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_07
python -m pytest -v
```

## What To Notice

The job logic is placed in a normal Python function.

The test passes input data to the function and checks the returned output.

Avoid putting all business logic directly inside notebooks or job entry points.
