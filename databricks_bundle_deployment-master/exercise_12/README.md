# Exercise 12: Tests Before Deployment

This exercise adds local tests before bundle validation and deployment.

Exercise 11 packaged code as a wheel. Exercise 12 focuses on checking business logic before deploying a Databricks job.

This exercise is designed for Databricks Free Edition serverless jobs.

## Project Files

```text
exercise_12/
  databricks.yml
  pyproject.toml
  notebooks/
    tested_logic_demo.py
  resources/
    tested_python_file_job.yml
  src/
    main.py
    customer_quality/
      __init__.py
      logic.py
  tests/
    test_customer_quality.py
```

## Notebook Demo Version

Use this notebook first:

```text
notebooks/tested_logic_demo.py
```

It shows the same filtering behavior manually.

The tested bundle version moves reusable logic into:

```text
src/customer_quality/logic.py
```

## What Gets Tested

The tests check:

1. Filtering by city.
2. Filtering by minimum ID.
3. Trimming city whitespace.
4. Rejecting an empty city.
5. Rejecting `min_id` less than `1`.

Open:

```text
tests/test_customer_quality.py
```

## Step 1: Move Into The Exercise Folder

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_12
```

## Step 2: Install Test Tooling

If `pytest` is not installed:

```powershell
python -m pip install pytest
```

## Step 3: Run Tests

```powershell
python -m pytest
```

Tests should pass before running bundle commands.

## Step 4: Validate The Bundle

```powershell
databricks bundle validate -t dev
```

This checks the deployment configuration.

## Step 5: Deploy

```powershell
databricks bundle deploy -t dev
```

## Step 6: Run

```powershell
databricks bundle run -t dev tested_python_file_job
```

## Step 7: Run With Different Parameters

```powershell
databricks bundle run -t dev --params city=London,min_id=3 tested_python_file_job
```

## Recommended Order

Use this order:

```powershell
python -m pytest
databricks bundle validate -t dev
databricks bundle deploy -t dev
databricks bundle run -t dev tested_python_file_job
```

## Key Idea

Tests check code behavior.

`databricks bundle validate` checks deployment configuration.

Use both before deploying.

## Clean Up

```powershell
databricks bundle destroy -t dev
```
