# Exercise 01: First Pytest Test

This exercise introduces pytest test discovery and simple assertions.

## Files

```text
exercise_01/
  calculator.py
  pytest.ini
  tests/
    test_calculator.py
```

## Run

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_01
python -m pytest -v
```

## What To Notice

Pytest finds files named `test_*.py`.

Pytest runs functions named `test_*`.

An `assert` passes when the expression is true.
