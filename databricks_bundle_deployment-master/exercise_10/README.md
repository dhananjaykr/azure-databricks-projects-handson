# Exercise 10: Permissions And Run Identity

This exercise shows where bundle permissions and run identity are configured.

Exercise 09 used Unity Catalog object names. Exercise 10 focuses on who can manage/run a deployed workflow and which identity the workflow runs as.

This exercise is designed for Databricks Free Edition. It uses the current workspace user as the run identity.

## Project Files

```text
exercise_10/
  databricks.yml
  notebooks/
    inspect_run_identity.py
  resources/
    permissions_run_as_job.yml
  src/
    inspect_run_identity.py
```

## Notebook Demo Version

Use this notebook first:

```text
notebooks/inspect_run_identity.py
```

The manual notebook lets you type the `run_as_user` value as a widget.

The bundle version sets that value from `${workspace.current_user.userName}`.

## Run Identity

Open:

```text
databricks.yml
```

The `dev` target contains:

```yaml
run_as:
  user_name: ${workspace.current_user.userName}
```

This means the deployed job runs as the current authenticated Databricks user.


## Permissions

The same target also contains:

```yaml
permissions:
  - user_name: ${workspace.current_user.userName}
    level: CAN_MANAGE
```

This grants the current user management permission over the deployed resources.

In a team workspace, you would usually grant groups lower permissions, such as `CAN_RUN` or `CAN_VIEW`.

## Job Configuration

Open:

```text
resources/permissions_run_as_job.yml
```

The job key is:

```yaml
permissions_run_as_job:
```

The job passes the run identity into the notebook:

```yaml
- name: run_as_user
  default: ${workspace.current_user.userName}
```

## Step 1: Move Into The Exercise Folder

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_10
```

## Step 2: Validate

```powershell
databricks bundle validate -t dev
```

Validation should show the resolved current user in the bundle graph.

## Step 3: Deploy

```powershell
databricks bundle deploy -t dev
```

## Step 4: Run

```powershell
databricks bundle run -t dev permissions_run_as_job
```

Expected output includes:

```text
configured_run_as_user: <your Databricks user>
```

## What To Check In Databricks

1. Open **Workflows**.
2. Open `exercise-10-permissions-run-as-job`.
3. Check job permissions.
4. Check the run-as identity.
5. Confirm the task output prints the configured run-as user.

## Key Idea

Permissions control who can view, run, or manage the job.

Run identity controls whose privileges the job uses when it accesses data and workspace resources.

## Clean Up

```powershell
databricks bundle destroy -t dev
```
