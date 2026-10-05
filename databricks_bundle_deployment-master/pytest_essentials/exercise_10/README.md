# Exercise 10: Environment Variables With monkeypatch

This exercise tests code that reads an environment variable.

## Files

```text
exercise_10/
  settings.py
  pytest.ini
  tests/
    test_settings.py
```

## Run

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_10
python -m pytest -v
```

## What To Notice

`monkeypatch.setenv` sets an environment variable for one test.

`monkeypatch.delenv` removes an environment variable for one test.

The real machine environment is not permanently changed.

This is useful for code driven by environment, catalog, schema, API endpoint, job parameters, and deployment target.
