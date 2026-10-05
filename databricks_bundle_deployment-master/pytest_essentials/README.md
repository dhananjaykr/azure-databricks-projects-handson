# Pytest Essentials

This folder contains small pytest exercises for normal modular Python code.

The goal is to become comfortable with testing Python functions before using the same testing habits inside Databricks Bundle projects.

## Setup

Open PowerShell and install the test tools once:

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials
python -m pip install -r requirements.txt
```

If `python` is not available, install Python first and reopen PowerShell.

## How To Run An Exercise

Each exercise is independent.

Move into one exercise folder and run pytest:

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_01
python -m pytest -v
```

Use the same pattern for every exercise.

## PyCharm Import Notes

For Exercises 01-11, the Python file is stored directly inside the exercise folder and the tests are stored under `tests/`.

Each of these exercises has this setting in `pytest.ini`:

```ini
pythonpath = .
```

When running from PyCharm, use the exercise folder as the working directory.

Example for Exercise 01:

```text
C:\Users\Sandeep\PycharmProjects\databricks_deployment\pytest_essentials\exercise_01
```

If PyCharm still shows a red underline on imports, right-click the current exercise folder and choose:

```text
Mark Directory as > Sources Root
```

## Exercise Sequence

| Exercise | Topic | Folder |
| --- | --- | --- |
| 01 | First pytest test | `exercise_01` |
| 02 | Reading a pytest failure | `exercise_02` |
| 03 | Parameterized tests | `exercise_03` |
| 04 | Business rule tests | `exercise_04` |
| 05 | Exception tests | `exercise_05` |
| 06 | Fixtures | `exercise_06` |
| 07 | Transformation tests | `exercise_07` |
| 08 | File tests with `tmp_path` | `exercise_08` |
| 09 | Configuration tests | `exercise_09` |
| 10 | Environment variable tests with `monkeypatch` | `exercise_10` |
| 11 | Mocking an external dependency | `exercise_11` |
| 12 | Small pipeline tests | `exercise_12` |
| 13 | Mocking the extraction layer | `exercise_13` |
| 14 | Unit and integration markers | `exercise_14` |
| 15 | Test coverage | `exercise_15` |

## Recommended Demonstration Order

Run the exercises in order.

The most important exercises for Databricks Bundle preparation are:

```text
exercise_03
exercise_06
exercise_07
exercise_09
exercise_10
exercise_11
exercise_12
exercise_13
exercise_14
exercise_15
```

These exercises map directly to bundle-based work:

```text
Python functions
pytest tests
bundle validate
bundle deploy
bundle run
```

## Folder Rule

Run tests from inside the exercise folder, not from the root `pytest_essentials` folder.

Each exercise contains its own code and tests so the examples stay simple and predictable.
