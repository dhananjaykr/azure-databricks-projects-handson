# Exercise 03: Multi-Task Job

This exercise deploys a Databricks Job with multiple tasks and dependencies.

Exercise 02 introduced job parameters. Exercise 03 keeps those parameters and adds task order.

This exercise is designed for Databricks Free Edition. It uses serverless job compute through a job environment. No custom cluster or node type is configured.

The job has three tasks:

| Task | Runs after | Purpose |
| --- | --- | --- |
| `validate_parameters` | Nothing | Checks the input values |
| `process_customers` | `validate_parameters` | Filters customer data |
| `summarize_run` | `process_customers` | Prints final run information |

## Project Files

```text
exercise_03/
  databricks.yml
  notebooks/
    01_validate_parameters.py
    02_process_customers.py
    03_summarize_run.py
  resources/
    multi_task_job.yml
  src/
    validate_parameters.py
    process_customers.py
    summarize_run.py
```

## Notebook Demo Version

Use these notebooks first when demonstrating the notebook-based multi-task job:

```text
notebooks/01_validate_parameters.py
notebooks/02_process_customers.py
notebooks/03_summarize_run.py
```

These are Databricks source notebook files. Import or create them as Databricks notebooks, then configure a multi-task job in the Jobs UI:

| Notebook | Task key to use in the UI | Runs after |
| --- | --- | --- |
| `01_validate_parameters.py` | `validate_parameters` | Nothing |
| `02_process_customers.py` | `process_customers` | `validate_parameters` |
| `03_summarize_run.py` | `summarize_run` | `process_customers` |

The notebook version reads parameters with widgets.

These notebooks are not used by the bundle. The bundle job uses the Python files in:

```text
src/
```

The notebook and bundle versions demonstrate the same task flow.

Notebook job setup in the Databricks UI:

1. Import or create all three notebooks from the `notebooks` folder.
2. Go to **Workflows**.
3. Create a new job.
4. Add job parameters:

```text
city = Pune
min_id = 1
```

5. Add notebook task `validate_parameters` using `01_validate_parameters.py`.
6. Add notebook task `process_customers` using `02_process_customers.py`.
7. Set `process_customers` to depend on `validate_parameters`.
8. Add notebook task `summarize_run` using `03_summarize_run.py`.
9. Set `summarize_run` to depend on `process_customers`.
10. Run the job and inspect the task graph.
11. Compare the UI task graph with the bundle `depends_on` configuration.

## What Changed From Exercise 02

Exercise 02 had one task.

Exercise 03 adds:

1. Three tasks in one job.
2. `depends_on` to control task order.
3. One shared serverless environment used by all tasks.
4. Dynamic job metadata passed into a task.

## Job Configuration

Open:

```text
resources/multi_task_job.yml
```

The job key is:

```yaml
multi_task_python_job:
```

This is the key used by the CLI when running the job.

The job parameters are the same pattern used in Exercise 02:

```yaml
parameters:
  - name: city
    default: ${var.default_city}
  - name: min_id
    default: ${var.default_min_id}
```

## Task 1: Validate Parameters

```yaml
- task_key: validate_parameters
  spark_python_task:
    python_file: ../src/validate_parameters.py
```

This task checks that:

1. `city` is not empty.
2. `min_id` is greater than or equal to `1`.

If this task fails, downstream tasks do not run.

## Task 2: Process Customers

```yaml
- task_key: process_customers
  depends_on:
    - task_key: validate_parameters
```

This task runs only after `validate_parameters` succeeds.

It uses:

```text
src/process_customers.py
```

## Task 3: Summarize Run

```yaml
- task_key: summarize_run
  depends_on:
    - task_key: process_customers
```

This task runs only after `process_customers` succeeds.

It receives normal job parameters:

```yaml
- "--city={{job.parameters.city}}"
- "--min_id={{job.parameters.min_id}}"
```

It also receives Databricks run metadata:

```yaml
- "--job_name={{job.name}}"
- "--job_run_id={{job.run_id}}"
```

These values are resolved by Databricks when the job run starts.

## Shared Serverless Environment

All three tasks use:

```yaml
environment_key: default
```

The serverless environment is defined once:

```yaml
environments:
  - environment_key: default
    spec:
      environment_version: "2"
```

This avoids repeating the environment definition under every task.

## Step 1: Move Into The Exercise Folder

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_03
```

Run all bundle commands from this folder.

## Step 2: Validate

```powershell
databricks bundle validate -t dev
```

This checks the bundle, job parameters, task dependencies, Python file paths, serverless environment, and workspace target.

## Step 3: Deploy

```powershell
databricks bundle deploy -t dev
```

This creates or updates the job named:

```text
exercise-03-multi-task-python-job
```

## Step 4: Run With Default Parameters

```powershell
databricks bundle run -t dev multi_task_python_job
```

Expected order:

```text
validate_parameters
process_customers
summarize_run
```

## Step 5: Run With Different Parameters

```powershell
databricks bundle run -t dev --params city=London,min_id=3 multi_task_python_job
```

No redeployment is needed for this step. Job parameters are resolved at run time.

## Step 6: Run One Task For Testing

Run only the processing task:

```powershell
databricks bundle run -t dev --only process_customers multi_task_python_job
```

Run the processing task and its upstream dependencies:

```powershell
databricks bundle run -t dev --only +process_customers multi_task_python_job
```

The `+` before the task key means Databricks also runs the tasks that `process_customers` depends on.

## What To Check In Databricks

1. Open the Databricks workspace.
2. Go to **Workflows**.
3. Open the job `exercise-03-multi-task-python-job`.
4. Open the latest run.
5. Check the task graph.
6. Confirm the task order:

```text
validate_parameters -> process_customers -> summarize_run
```

## Key Idea

Use `depends_on` when one task must finish before another task starts.

In this exercise, the dependency chain is:

```text
validate_parameters
  -> process_customers
  -> summarize_run
```

This exercise controls execution order. It does not pass data between tasks yet.

## Clean Up

```powershell
databricks bundle destroy -t dev
```
