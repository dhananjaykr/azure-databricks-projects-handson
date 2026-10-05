# Exercise 08: File Tests With tmp_path

This exercise writes a file into a pytest temporary directory.

## Files

```text
exercise_08/
  file_processor.py
  pytest.ini
  tests/
    test_file_processor.py
```

## Run

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_08
python -m pytest -v
```

## What To Notice

`tmp_path` gives each test a temporary folder.

The test can write files without changing project files.

This is useful for config files, JSON files, CSV files, temporary outputs, and test datasets.
