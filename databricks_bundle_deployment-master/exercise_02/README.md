# Exercise 02: Job Parameters

This exercise deploys a Databricks Job that accepts parameters at run time.

This exercise is designed for Databricks Free Edition. It uses serverless job compute through a job environment. No custom cluster or node type is configured.

Exercise 01 used fixed code. Exercise 02 keeps the same basic deployment flow and adds two job parameters:

| Parameter | Default value | Meaning |
| --- | --- | --- |
| `city` | `Pune` | City to keep in the output |
| `min_id` | `1` | Minimum customer ID to keep |

## Project Files

```text
exercise_02/
  databricks.yml
  notebooks/
    parameterized_job_notebook.py
  resources/
    parameterized_job.yml
  src/
    main.py
```

## Notebook Demo Version

Use this notebook first when demonstrating the notebook-based job:

```text
notebooks/parameterized_job_notebook.py
```

This is a Databricks source notebook file. Import or create it as a Databricks notebook, then configure a notebook task in the Jobs UI.

The notebook version reads parameters with widgets:

```python
dbutils.widgets.text("city", "Pune", "City")
dbutils.widgets.text("min_id", "1", "Minimum customer ID")

city = dbutils.widgets.get("city")
min_id = int(dbutils.widgets.get("min_id"))
```

This notebook is not used by the bundle. The bundle job uses:

```text
src/main.py
```

The bundle Python file version reads parameters with command-line arguments and `argparse`.

Notebook job setup in the Databricks UI:

1. Import or create the notebook from `notebooks/parameterized_job_notebook.py`.
2. Go to **Workflows**.
3. Create a new job.
4. Add one notebook task.
5. Select the imported notebook.
6. Add job parameters:

```text
city = Pune
min_id = 1
```

7. Run the job.
8. Use **Run now with different parameters** and change the values.
9. Compare this with the bundle run command that uses `--params`.

## What Changed From Exercise 01

Exercise 01 had one Python file task with no input values.

Exercise 02 adds:

1. Bundle variables for default values.
2. Job parameters on the Databricks Job.
3. Python script arguments passed into `src/main.py`.
4. Runtime parameter overrides from the Databricks CLI.
5. A serverless job environment for Free Edition.

## Main Bundle File

Open:

```text
databricks.yml
```

The bundle variables are:

```yaml
variables:
  default_city:
    default: Pune
  default_min_id:
    default: "1"
```

These values are resolved when the bundle is deployed.

There are no node type or Spark runtime variables in this exercise because Free Edition uses serverless compute.

## Job Configuration

Open:

```text
resources/parameterized_job.yml
```

The job key is:

```yaml
parameterized_python_job:
```

This is the key used by the CLI when running the job.

The job parameters are:

```yaml
parameters:
  - name: city
    default: ${var.default_city}
  - name: min_id
    default: ${var.default_min_id}
```

The task passes those job parameters to the Python file:

```yaml
spark_python_task:
  python_file: ../src/main.py
  parameters:
    - "--city={{job.parameters.city}}"
    - "--min_id={{job.parameters.min_id}}"
environment_key: default
```

`{{job.parameters.city}}` is resolved when the job run starts.

`{{job.parameters.min_id}}` is also resolved when the job run starts.

`${var.default_city}` is resolved when the bundle is deployed.

`${var.default_min_id}` is also resolved when the bundle is deployed.

The serverless environment is:

```yaml
environments:
  - environment_key: default
    spec:
      environment_version: "2"
```

## Python Code

Open:

```text
src/main.py
```

The script uses `argparse` to read command-line arguments:

```python
parser.add_argument("--city", required=True)
parser.add_argument("--min_id", required=True, type=int)
```

This is why the YAML task passes:

```text
--city
--min_id
```

This is the normal pattern for a Python script task because `spark_python_task.parameters` are passed to the Python file as command-line arguments.

Do not use `dbutils.widgets.get()` in this exercise. Widgets are the common pattern for notebook tasks, but this exercise is a Python file task.

The notebook demo file does use `dbutils.widgets.get()` because it is a notebook task example.

## Parameter Name Rule

Use the same parameter name at each layer:

| Layer | Name |
| --- | --- |
| Job parameter | `min_id` |
| Dynamic reference | `{{job.parameters.min_id}}` |
| Python script flag | `--min_id` |
| Python variable | `args.min_id` |

Keeping the same name makes the parameter flow easier to trace.

## Step 1: Move Into The Exercise Folder

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_02
```

Run all bundle commands from this folder.

## Step 2: Validate

```powershell
databricks bundle validate -t dev
```

This checks that the bundle, variables, job parameters, task configuration, serverless environment, and workspace target are valid.

## Step 3: Deploy

```powershell
databricks bundle deploy -t dev
```

This creates or updates the job named:

```text
exercise-02-parameterized-python-job
```

## Step 4: Run With Default Parameters

```powershell
databricks bundle run -t dev parameterized_python_job
```

Expected parameter values:

```text
Raw command-line arguments
['--city=Pune', '--min_id=1']
city: Pune
min_id: 1
```

## Step 5: Run With Different Parameters

```powershell
databricks bundle run -t dev --params city=Mumbai,min_id=2 parameterized_python_job
```

Expected parameter values:

```text
Raw command-line arguments
['--city=Mumbai', '--min_id=2']
city: Mumbai
min_id: 2
```

No redeployment is needed for this step. Job parameters are resolved at run time.

## Step 6: Try A Bad Parameter Value

Run with an invalid `min_id`:

```powershell
databricks bundle run -t dev --params city=Pune,min_id=0 parameterized_python_job
```

Expected result:

```text
ValueError: min_id must be greater than or equal to 1
```

This confirms that the value reached the Python script and was checked by the script.

## What To Check In Databricks

1. Open the Databricks workspace.
2. Go to **Workflows**.
3. Open the job `exercise-02-parameterized-python-job`.
4. Open a job run.
5. Check the **Parameters** section.
6. Open the task output for `filter_customers`.
7. Confirm that the task output shows the raw command-line arguments.

## Key Idea

Use bundle variables for values that change by environment.

Use job parameters for values that change by run.

In this exercise:

| Value | Type | Resolved when |
| --- | --- | --- |
| `city` | Job parameter | Run time |
| `min_id` | Job parameter | Run time |

## Clean Up

```powershell
databricks bundle destroy -t dev
```
