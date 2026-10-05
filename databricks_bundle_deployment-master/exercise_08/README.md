# Exercise 08: Shared Bundle Variables

This exercise shows how to use bundle variables as shared configuration.

Exercise 06 used target-specific variables. Exercise 08 uses variables in multiple places: job name, tags, and job parameter defaults.

This exercise is designed for Databricks Free Edition.

## Project Files

```text
exercise_08/
  databricks.yml
  notebooks/
    shared_variables_report.py
  resources/
    shared_variables_job.yml
  src/
    shared_variables_report.py
```

## Notebook Demo Version

Use this notebook first:

```text
notebooks/shared_variables_report.py
```

It lets you type all values manually with widgets.

The bundle version shows how the same values can come from bundle variables.

## Bundle Variables

Open:

```text
databricks.yml
```

The variables are:

```yaml
report_title
report_owner
environment_label
default_city
default_min_id
```

The `dev` target and `qa_like` target override some values.

## Reusing Variables

Open:

```text
resources/shared_variables_job.yml
```

The same variable values are reused in:

1. Job name.
2. Job tags.
3. Job parameter defaults.

Example:

```yaml
name: exercise-08-${var.environment_label}-shared-variables-job
```

Another example:

```yaml
tags:
  environment: ${var.environment_label}
  owner: ${var.report_owner}
```

## Step 1: Move Into The Exercise Folder

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_08
```

## Step 2: Validate And Run Dev

```powershell
databricks bundle validate -t dev
databricks bundle deploy -t dev
databricks bundle run -t dev shared_variables_job
```

Expected values:

```text
environment_label: dev
city: Pune
min_id: 1
```

## Step 3: Validate And Run QA-Like

```powershell
databricks bundle validate -t qa_like
databricks bundle deploy -t qa_like
databricks bundle run -t qa_like shared_variables_job
```

Expected values:

```text
environment_label: qa_like
city: London
min_id: 3
```

## Step 4: Override Job Parameters At Run Time

```powershell
databricks bundle run -t dev --params city=Mumbai,min_id=2 shared_variables_job
```

This overrides job parameters for that run only.

## Key Idea

Bundle variables configure the deployed job.

Job parameters configure an individual run.

Use bundle variables for values that belong to an environment or deployment.

Use job parameters for values that can change every run.

## Clean Up

```powershell
databricks bundle destroy -t dev
databricks bundle destroy -t qa_like
```
