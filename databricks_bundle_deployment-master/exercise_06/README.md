# Exercise 06: Multiple Bundle Targets

This exercise uses two bundle targets.

Exercise 05 added a schedule. Exercise 06 focuses on deployment targets: the same bundle can deploy with different values depending on the selected target.

This exercise is designed for Databricks Free Edition. Both targets point to the same workspace for training.

## Project Files

```text
exercise_06/
  databricks.yml
  notebooks/
    targeted_customer_report.py
  resources/
    targeted_job.yml
  src/
    targeted_customer_report.py
```

## Notebook Demo Version

Use this notebook first for the manual notebook-job demonstration:

```text
notebooks/targeted_customer_report.py
```

Set widget values manually:

```text
target_label = manual_ui
city = Pune
min_id = 1
```

The bundle version then shows how target-specific values are defined in YAML.

## Bundle Targets

Open:

```text
databricks.yml
```

The bundle has two targets:

```yaml
targets:
  dev:
    mode: development
    default: true

  prod_like:
    mode: production
```

For training, both targets use the same workspace URL.

In a real project, `dev` and production usually point to different workspaces or use different identities.

## Target-Specific Variables

The `dev` target uses:

```yaml
target_label: dev
default_city: Pune
default_min_id: "1"
```

The `prod_like` target uses:

```yaml
target_label: prod_like
default_city: Mumbai
default_min_id: "2"
```

These variables become job parameter defaults.

## Job Configuration

Open:

```text
resources/targeted_job.yml
```

The job key is:

```yaml
targeted_notebook_job:
```

The job name uses the target label:

```yaml
name: exercise-06-${var.target_label}-targeted-notebook-job
```

This makes the deployed jobs easy to distinguish.

## Step 1: Move Into The Exercise Folder

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_06
```

## Step 2: Validate The Dev Target

```powershell
databricks bundle validate -t dev
```

## Step 3: Deploy And Run The Dev Target

```powershell
databricks bundle deploy -t dev
databricks bundle run -t dev targeted_notebook_job
```

Expected values:

```text
target_label: dev
city: Pune
min_id: 1
```

## Step 4: Validate The Production-Like Target

```powershell
databricks bundle validate -t prod_like
```

## Step 5: Deploy And Run The Production-Like Target

```powershell
databricks bundle deploy -t prod_like
databricks bundle run -t prod_like targeted_notebook_job
```

Expected values:

```text
target_label: prod_like
city: Mumbai
min_id: 2
```

## Key Idea

Targets let the same bundle deploy with different settings.

Use `-t dev` or `-t prod_like` to choose the target.

## Clean Up

```powershell
databricks bundle destroy -t dev
databricks bundle destroy -t prod_like
```
