# Exercise 03: Parameterized Tests

This exercise tests one function with many input values.

## Files

```text
exercise_03/
  calculator.py
  pytest.ini
  tests/
    test_calculator.py
```

## Run

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_03
python -m pytest -v
```

## What To Notice

`pytest.mark.parametrize` runs the same test logic for multiple cases.

This pattern is useful when testing transformation rules against several input and expected-output combinations.
