# Exercise 05: Scheduled Job

This exercise deploys a Databricks notebook job with a schedule by using a bundle.

Exercise 04 introduced a bundle-deployed notebook task. Exercise 05 adds the `schedule` block.

This exercise is designed for Databricks Free Edition. It uses serverless job compute and does not configure a custom cluster.

## Project Files

```text
exercise_05/
  databricks.yml
  notebooks/
    scheduled_customer_report.py
  resources/
    scheduled_job.yml
  src/
    scheduled_customer_report.py
```

## Notebook Demo Version

Use this notebook first when demonstrating the notebook-based job manually:

```text
notebooks/scheduled_customer_report.py
```

Import or create it as a Databricks notebook, then run it manually with widgets.

The schedule is not part of the manual notebook file. The schedule is defined in the bundle resource YAML.

## Bundle Version

The bundle deploys this notebook:

```text
src/scheduled_customer_report.py
```

The bundle job is defined here:

```text
resources/scheduled_job.yml
```

The job key is:

```yaml
scheduled_notebook_job:
```

The notebook task is:

```yaml
tasks:
  - task_key: run_scheduled_customer_report
    notebook_task:
      notebook_path: ../src/scheduled_customer_report.py
```

## Schedule Configuration

The schedule is:

```yaml
schedule:
  quartz_cron_expression: ${var.schedule_quartz_cron_expression}
  timezone_id: ${var.schedule_timezone_id}
  pause_status: ${var.schedule_pause_status}
```

The defaults are in `databricks.yml`:

```yaml
schedule_quartz_cron_expression:
  default: "0 0 9 * * ?"
schedule_timezone_id:
  default: Asia/Kolkata
schedule_pause_status:
  default: PAUSED
```

This means the schedule is configured for 9:00 AM Asia/Kolkata, but it is paused by default.

Keeping the schedule paused is safer for a training exercise. Learners can inspect the job first, then intentionally change `schedule_pause_status` to `UNPAUSED`.

## Step 1: Move Into The Exercise Folder

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_05
```

## Step 2: Validate

```powershell
databricks bundle validate -t dev
```

This checks the bundle, notebook path, job parameters, schedule block, and workspace target.

## Step 3: Deploy

```powershell
databricks bundle deploy -t dev
```

This creates or updates:

```text
exercise-05-scheduled-notebook-job
```

## Step 4: Inspect The Schedule

In Databricks:

1. Open **Workflows**.
2. Open `exercise-05-scheduled-notebook-job`.
3. Check the schedule.
4. Confirm the schedule is paused.

## Step 5: Run Manually

```powershell
databricks bundle run -t dev scheduled_notebook_job
```

This runs the job immediately, even though the schedule is paused.

## Step 6: Run With Different Parameters

```powershell
databricks bundle run -t dev --params city=London,min_id=3 scheduled_notebook_job
```

The schedule controls when the job runs automatically. Job parameters still control what values the run uses.

## Step 7: Enable The Schedule

Edit `databricks.yml`:

```yaml
schedule_pause_status:
  default: UNPAUSED
```

Then redeploy:

```powershell
databricks bundle validate -t dev
databricks bundle deploy -t dev
```

The job will then run automatically according to the schedule.

## Key Idea

Manual run and scheduled run are different triggers for the same job.

The task definition says what runs.

The schedule says when it runs automatically.

## Clean Up

```powershell
databricks bundle destroy -t dev
```
