# Exercise 07: Workspace Deployment Paths

This exercise shows where bundle files are deployed in the Databricks workspace.

Exercise 06 introduced targets. Exercise 07 adds an explicit `workspace.root_path`.

This exercise is designed for Databricks Free Edition.

## Project Files

```text
exercise_07/
  databricks.yml
  notebooks/
    inspect_workspace_paths.py
  resources/
    workspace_path_job.yml
  src/
    inspect_workspace_paths.py
```

## Notebook Demo Version

Use this notebook first for the manual demonstration:

```text
notebooks/inspect_workspace_paths.py
```

The manual notebook uses widgets where you can paste path values.

The bundle version passes the actual bundle path substitutions automatically.

## Workspace Root Path

Open:

```text
databricks.yml
```

The `dev` target defines:

```yaml
workspace:
  root_path: /Workspace/Users/${workspace.current_user.userName}/.bundle_training/${bundle.name}/${bundle.target}
```

This controls where the bundle is deployed in the Databricks workspace.

## Bundle Substitutions

Open:

```text
resources/workspace_path_job.yml
```

The job passes these values into the notebook:

```yaml
parameters:
  - name: bundle_name
    default: ${bundle.name}
  - name: bundle_target
    default: ${bundle.target}
  - name: workspace_root_path
    default: ${workspace.root_path}
  - name: workspace_file_path
    default: ${workspace.file_path}
```

These are bundle substitutions. Databricks resolves them during deployment and run.

## Step 1: Move Into The Exercise Folder

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_07
```

## Step 2: Validate

```powershell
databricks bundle validate -t dev
```

## Step 3: Deploy

```powershell
databricks bundle deploy -t dev
```

After deployment, look in the workspace under:

```text
/Workspace/Users/<your-user>/.bundle_training/exercise_07_workspace_paths_bundle/dev
```

## Step 4: Run

```powershell
databricks bundle run -t dev workspace_path_job
```

The task output prints:

```text
bundle_name
bundle_target
workspace_root_path
workspace_file_path
```

## Key Idea

`workspace.root_path` controls the deployment root.

`${workspace.file_path}` points to where synced files are available for the deployed bundle.

## Clean Up

```powershell
databricks bundle destroy -t dev
```
