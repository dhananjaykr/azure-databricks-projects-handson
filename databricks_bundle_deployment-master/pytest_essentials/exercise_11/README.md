# Exercise 11: Mock An External Dependency

This exercise tests code without calling a real external service.

## Files

```text
exercise_11/
  customer_service.py
  pytest.ini
  tests/
    test_customer_service.py
```

## Run

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_11
python -m pytest -v
```

## What To Notice

The test uses `Mock` instead of a real API client.

The test checks the returned data and checks that the API method was called correctly.

This pattern applies to Databricks APIs, cloud storage clients, database clients, REST APIs, and secret managers.
