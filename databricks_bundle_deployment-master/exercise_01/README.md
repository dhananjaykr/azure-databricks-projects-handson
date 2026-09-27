# Exercise 01: Simple Databricks Job Deployment

This exercise deploys a small PySpark file as a Databricks Job by using a Databricks bundle.

This exercise is designed for Databricks Free Edition. It uses serverless job compute. No custom cluster, node type, Spark runtime, or Unity Catalog access mode is configured here.

## Notebook Workflow Compared To Bundle Workflow

| Notebook workflow | Bundle workflow in this exercise |
| --- | --- |
| Write code in notebook cells | Write code in `src/main.py` |
| Click **Run all** | Run the deployed job |
| Databricks provides compute | The job uses serverless compute |
| Job is managed manually in UI | Job is defined in YAML and deployed |

## Project Location

Use this folder:

```powershell
C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_01
```

Move into the exercise folder:

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_01
```

Run all Databricks bundle commands from this folder.

## Project Files

```text
exercise_01/
  databricks.yml
  notebooks/
    simple_job_notebook.py
  resources/
    simple_job.yml
  src/
    main.py
```

## Notebook Demo Version

Use this notebook first when demonstrating the notebook-based job:

```text
notebooks/simple_job_notebook.py
```

This is a Databricks source notebook file. Import or create it as a Databricks notebook, then run it manually or configure it as a notebook task in the Jobs UI.

This notebook is not used by the bundle. The bundle job uses:

```text
src/main.py
```

The notebook and bundle versions do the same work so learners can compare both approaches.

Notebook job setup in the Databricks UI:

1. Import or create the notebook from `notebooks/simple_job_notebook.py`.
2. Go to **Workflows**.
3. Create a new job.
4. Add one notebook task.
5. Select the imported notebook.
6. Run the job.
7. Compare the notebook task output with the bundle job output.

## `src/main.py`

This is the PySpark code that the Databricks Job runs.

What it does:

1. Starts or gets a Spark session.
2. Creates a small in-memory customer dataset.
3. Converts the data into a Spark DataFrame.
4. Prints the DataFrame.
5. Prints the total record count.

Important line:

```python
spark = SparkSession.builder.getOrCreate()
```

In a notebook, Databricks usually provides the Spark session automatically. In a Python file, the script asks Spark for the active session.

## `databricks.yml`

This is the main bundle file.

```yaml
bundle:
  name: simple_databricks_bundle
```

The bundle name identifies this deployment.

```yaml
include:
  - resources/*.yml
```

This tells Databricks to load resource definitions from the `resources` folder.

```yaml
targets:
  dev:
    mode: development
    default: true
    workspace:
      host: https://adb-7405609765733903.3.azuredatabricks.net
```

This defines the `dev` target and points it to the Databricks workspace.

## `resources/simple_job.yml`

This file defines the Databricks Job.

```yaml
resources:
  jobs:
    simple_python_job:
```

`simple_python_job` is the job key. Use this key when running the job from the command line.

The job display name is:

```yaml
name: simple-python-job
```

The task is:

```yaml
tasks:
  - task_key: run_python_task
    spark_python_task:
      python_file: ../src/main.py
    environment_key: default
```

This means:

1. The job has one task.
2. The task runs a Python file.
3. The Python file is `src/main.py`.
4. The task uses the serverless environment named `default`.

The serverless environment is:

```yaml
environments:
  - environment_key: default
    spec:
      environment_version: "2"
```

This is the Free Edition-friendly compute pattern. Databricks manages the serverless runtime. You do not choose a VM node type in these exercises.

## Full Deployment Sequence

### Step 1: Check The Databricks CLI

```powershell
databricks -v
```

If the command is not recognized, install the Databricks CLI first.

### Step 2: Log In To The Workspace

```powershell
databricks auth login --host https://adb-7405609765733903.3.azuredatabricks.net
```

This connects the local CLI to the Databricks workspace.

### Step 3: Validate The Bundle

```powershell
databricks bundle validate -t dev
```

This checks:

1. `databricks.yml`
2. `resources/simple_job.yml`
3. Python file paths
4. The `dev` target
5. The serverless job environment

Validation does not create a job.

### Step 4: Deploy The Bundle

```powershell
databricks bundle deploy -t dev
```

This creates or updates the job in Databricks.

After deployment:

1. Open the Databricks workspace.
2. Go to **Workflows**.
3. Open **Jobs**.
4. Look for `simple-python-job`.

### Step 5: Run The Job

```powershell
databricks bundle run -t dev simple_python_job
```

This starts the job run on serverless compute.

Expected output includes:

```text
Customer Data
Total records: 4
Job completed successfully.
```

## Local Change Workflow

Use this sequence whenever you change files:

```powershell
databricks bundle validate -t dev
databricks bundle deploy -t dev
databricks bundle run -t dev simple_python_job
```

## Important Names

| Name | Where it appears | Meaning |
| --- | --- | --- |
| `simple_databricks_bundle` | `databricks.yml` | Bundle name |
| `dev` | `databricks.yml` | Deployment target |
| `simple_python_job` | `resources/simple_job.yml` | Job key used by the CLI |
| `simple-python-job` | Databricks UI | Job display name |
| `run_python_task` | Databricks UI | Task inside the job |
| `default` | `resources/simple_job.yml` | Serverless environment key |

## Common First-Time Issues

### `databricks` is not recognized

The Databricks CLI is not installed or PowerShell was opened before installation.

Fix:

1. Install the Databricks CLI.
2. Close PowerShell.
3. Open PowerShell again.
4. Run `databricks -v`.

### Authentication error

The CLI is not logged in to the workspace.

Fix:

```powershell
databricks auth login --host https://adb-7405609765733903.3.azuredatabricks.net
```

### Job does not show custom cluster settings

That is expected in this exercise.

Exercise 01 uses serverless job compute for Databricks Free Edition. Custom job clusters, node types, and Unity Catalog access mode settings are covered separately in the advanced Unity Catalog job-cluster exercise.

## Clean Up

```powershell
databricks bundle destroy -t dev
```

This removes the deployed bundle resources for the `dev` target.
