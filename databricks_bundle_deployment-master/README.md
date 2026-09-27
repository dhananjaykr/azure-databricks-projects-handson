# Databricks Deployment Exercises

This folder is the root workspace for Databricks deployment exercises.

Exercises 01-14 are designed for Databricks Free Edition. They should use serverless job compute, not custom job clusters.

The Unity Catalog job-cluster topic is handled as a separate advanced exercise because it requires a workspace where custom/Dedicated job clusters are available.

The current exercise files point to this workspace:

```text
https://adb-7405609765733903.3.azuredatabricks.net
```

Candidates using their own Databricks Free Edition workspace should replace `workspace.host` in each exercise's `databricks.yml` with their own workspace URL before validating or deploying.

Each exercise should live in its own folder:

```text
databricks_deployment/
  README.md
  exercise_01/
    README.md
    databricks.yml
    notebooks/
    resources/
    src/
  exercise_02/
    README.md
    databricks.yml
    notebooks/
    resources/
    src/
  exercise_03/
    README.md
    databricks.yml
    notebooks/
    resources/
    src/
  exercise_04/
    README.md
    databricks.yml
    notebooks/
    resources/
    src/
  exercise_05/
    README.md
    databricks.yml
    notebooks/
    resources/
    src/
  exercise_06/
    README.md
    databricks.yml
    notebooks/
    resources/
    src/
  exercise_07/
    README.md
    databricks.yml
    notebooks/
    resources/
    src/
  exercise_08/
    README.md
    databricks.yml
    notebooks/
    resources/
    src/
  exercise_09/
    README.md
    databricks.yml
    notebooks/
    resources/
    src/
  exercise_10/
    README.md
    databricks.yml
    notebooks/
    resources/
    src/
  exercise_11/
    README.md
    databricks.yml
    notebooks/
    resources/
    src/
  exercise_12/
    README.md
    databricks.yml
    notebooks/
    resources/
    src/
    tests/
```

Current exercises:

| Exercise | Purpose | Folder | Job key |
| --- | --- | --- | --- |
| Exercise 01 | Deploy a simple PySpark file as a serverless Databricks Job | `exercise_01` | `simple_python_job` |
| Exercise 02 | Add job parameters to a serverless Databricks Job | `exercise_02` | `parameterized_python_job` |
| Exercise 03 | Deploy a serverless multi-task Databricks Job with dependencies | `exercise_03` | `multi_task_python_job` |
| Exercise 04 | Deploy a notebook task through a bundle | `exercise_04` | `notebook_task_job` |
| Exercise 05 | Add a schedule to a bundle-deployed notebook job | `exercise_05` | `scheduled_notebook_job` |
| Exercise 06 | Use multiple bundle targets with different defaults | `exercise_06` | `targeted_notebook_job` |
| Exercise 07 | Control and inspect bundle workspace deployment paths | `exercise_07` | `workspace_path_job` |
| Exercise 08 | Reuse shared bundle variables across a job | `exercise_08` | `shared_variables_job` |
| Exercise 09 | Write and read a Unity Catalog table from a bundle job | `exercise_09` | `unity_catalog_table_job` |
| Exercise 10 | Configure job permissions and run identity | `exercise_10` | `permissions_run_as_job` |
| Exercise 11 | Build and deploy a Python wheel task | `exercise_11` | `python_wheel_package_job` |
| Exercise 12 | Run local tests before bundle deployment | `exercise_12` | `tested_python_file_job` |

Planned advanced exercise:

| Exercise | Purpose | Compute |
| --- | --- | --- |
| Advanced Unity Catalog Job Cluster | Deploy a job on a Dedicated access mode cluster with Unity Catalog access | Custom job cluster, not Free Edition |

## How To Work With An Exercise

Always move into the exercise folder before running Databricks bundle commands.

For example, to work with Exercise 01:

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_01
```

Use the same sequence for every exercise:

```powershell
databricks bundle validate -t dev
databricks bundle deploy -t dev
databricks bundle run -t dev <job_key>
```

Each exercise README gives the correct `<job_key>`.

Each exercise is independent. This means one exercise can have its own `databricks.yml`, job configuration, source code, and README without needing a separate PyCharm project.

## Teaching Sequence

Each exercise can be demonstrated in two ways:

1. Notebook version first.
2. Bundle version second.

The notebook version is stored in:

```text
exercise_XX/notebooks/
```

The bundle version is stored in:

```text
exercise_XX/databricks.yml
exercise_XX/resources/
exercise_XX/src/
```

The notebook files are for manual notebook-job demonstration only. They are not referenced from the bundle YAML files.

When a bundle exercise deploys a notebook task, the bundle references the notebook source under `src/`. The `notebooks/` folder remains the manual UI demo version.

## Free Edition Rule

For Exercises 01-14:

1. Use serverless job compute.
2. For Python file tasks, use `environment_key` under each task.
3. For Python file tasks, define `environments` under the job.
4. For notebook tasks, use `notebook_task` and omit custom cluster configuration.
5. Do not configure `job_clusters`.
6. Do not configure `node_type_id`.
7. Do not configure `spark_version`.
8. Do not configure `data_security_mode`.

Custom job clusters and Unity Catalog access modes are saved for the advanced Unity Catalog job-cluster exercise.

## Folder Rule

Keep each exercise self-contained:

```text
exercise_XX/
  README.md
  databricks.yml
  notebooks/
  resources/
  src/
```

Run commands from inside the exercise folder, not from the root `databricks_deployment` folder.
