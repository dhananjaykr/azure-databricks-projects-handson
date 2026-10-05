# Exercise 11: Python Wheel Deployment

This exercise packages Python code as a wheel and runs it as a Databricks Python wheel task.

Exercise 10 focused on identity and permissions. Exercise 11 focuses on deployable Python packages.

This exercise is designed for Databricks Free Edition serverless jobs. Python wheel tasks require a job environment.

## Project Files

```text
exercise_11/
  databricks.yml
  setup.py
  notebooks/
    wheel_logic_demo.py
  resources/
    python_wheel_job.yml
  src/
    customer_wheel_job/
      __init__.py
      main.py
```

## Notebook Demo Version

Use this notebook first:

```text
notebooks/wheel_logic_demo.py
```

It demonstrates the same logic before packaging.

The bundle version packages the code under:

```text
src/customer_wheel_job/
```

## Package Configuration

Open:

```text
setup.py
```

The package name is:

```python
name="customer_wheel_job"
```

The entry point is:

```python
"main=customer_wheel_job.main:main"
```

This tells Databricks which function to run from the wheel.

## Artifact Configuration

Open:

```text
databricks.yml
```

The bundle artifact is:

```yaml
artifacts:
  default:
    type: whl
    build: python setup.py bdist_wheel
    path: .
```

During deployment, the Databricks CLI builds the wheel and uploads it with the bundle artifacts.

## Job Configuration

Open:

```text
resources/python_wheel_job.yml
```

The job key is:

```yaml
python_wheel_package_job:
```

The task type is:

```yaml
python_wheel_task:
  package_name: customer_wheel_job
  entry_point: main
```

The serverless job environment installs the wheel:

```yaml
environments:
  - environment_key: default
    spec:
      environment_version: "4"
      dependencies:
        - ../dist/*.whl
```

## Step 1: Move Into The Exercise Folder

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_11
```

## Step 2: Build The Wheel Locally

```powershell
python setup.py bdist_wheel
```

Expected result:

```text
dist/customer_wheel_job-0.0.1-py3-none-any.whl
```

If `python` is not available locally, install Python first.

## Step 3: Validate

```powershell
databricks bundle validate -t dev
```

## Step 4: Deploy

```powershell
databricks bundle deploy -t dev
```

Deployment builds and uploads the wheel artifact.

## Step 5: Run

```powershell
databricks bundle run -t dev python_wheel_package_job
```

## Step 6: Run With Different Parameters

```powershell
databricks bundle run -t dev --params city=London,min_id=3 python_wheel_package_job
```

## Key Idea

A Python wheel task runs packaged Python code.

This is closer to production-style deployment than running loose Python files.

When the code changes, update the package version or rebuild/redeploy so the serverless environment receives the new wheel.

## Clean Up

```powershell
databricks bundle destroy -t dev
```
