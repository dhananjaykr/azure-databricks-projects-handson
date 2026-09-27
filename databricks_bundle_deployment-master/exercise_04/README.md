# Exercise 04: Notebook Task Deployment

This exercise deploys a Databricks notebook task by using a bundle.

Exercises 01-03 used Python file tasks. Exercise 04 introduces a bundle job that runs a notebook.

This exercise is designed for Databricks Free Edition. It uses serverless job compute by omitting custom cluster configuration.

## Project Files

```text
exercise_04/
  databricks.yml
  notebooks/
    customer_filter_notebook.py
  resources/
    notebook_job.yml
  src/
    customer_filter_notebook.py
```

## Notebook Demo Version

Use this notebook first when demonstrating the notebook-based job manually:

```text
notebooks/customer_filter_notebook.py
```

Import or create it as a Databricks notebook, then configure it as a notebook task in the Jobs UI.

Add job parameters in the UI:

```text
city = Pune
min_id = 1
```

The notebook reads parameters with widgets:

```python
dbutils.widgets.get("city")
dbutils.widgets.get("min_id")
```

## Bundle Version

The bundle deploys this notebook file:

```text
src/customer_filter_notebook.py
```

The bundle job is defined here:

```text
resources/notebook_job.yml
```

The job key is:

```yaml
notebook_task_job:
```

The task uses `notebook_task`:

```yaml
tasks:
  - task_key: run_customer_notebook
    notebook_task:
      notebook_path: ../src/customer_filter_notebook.py
```

For a serverless notebook job, there is no `environment_key` and no `job_clusters` block.

## Why This Is Different From Python File Tasks

| Python file task | Notebook task |
| --- | --- |
| Uses `spark_python_task` | Uses `notebook_task` |
| Reads arguments with `argparse` | Reads parameters with widgets |
| Needs `environment_key` for serverless | Can run serverless without a cluster block |
| Points to `src/main.py` style files | Points to a Databricks notebook source file |

## Step 1: Move Into The Exercise Folder

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_04
```

## Step 2: Validate

```powershell
databricks bundle validate -t dev
```

This checks the bundle, notebook path, job parameters, and workspace target.

## Step 3: Deploy

```powershell
databricks bundle deploy -t dev
```

This creates or updates:

```text
exercise-04-notebook-task-job
```

## Step 4: Run With Default Parameters

```powershell
databricks bundle run -t dev notebook_task_job
```

Expected parameter values:

```text
city: Pune
min_id: 1
```

## Step 5: Run With Different Parameters

```powershell
databricks bundle run -t dev --params city=Mumbai,min_id=2 notebook_task_job
```

No redeployment is needed. Job parameters are resolved at run time.

## What To Check In Databricks

1. Open **Workflows**.
2. Open the job `exercise-04-notebook-task-job`.
3. Open the task `run_customer_notebook`.
4. Confirm the task type is notebook.
5. Open the latest run output.
6. Confirm the widget parameter values changed when using `--params`.

## Key Idea

Use `notebook_task` when the deployed job should run a notebook.

Use `spark_python_task` when the deployed job should run a Python file.

## Clean Up

```powershell
databricks bundle destroy -t dev
```
