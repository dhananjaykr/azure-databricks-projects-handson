# Exercise 09: Unity Catalog Table Job

This exercise writes and reads a Unity Catalog managed table from a bundle-deployed job.

Exercise 08 focused on shared variables. Exercise 09 uses variables for catalog, schema, and table names.

This exercise is designed for Databricks Free Edition with serverless jobs. It does not use a custom Unity Catalog-enabled job cluster.

## Project Files

```text
exercise_09/
  databricks.yml
  notebooks/
    write_and_read_uc_table.py
  resources/
    unity_catalog_table_job.yml
  src/
    write_and_read_uc_table.py
```

## Notebook Demo Version

Use this notebook first:

```text
notebooks/write_and_read_uc_table.py
```

Set widget values for a catalog and schema where your user can create or replace a table.

Default values:

```text
catalog_name = workspace
schema_name = default
table_name = exercise_09_customers
city = Pune
min_id = 1
```

If your workspace uses different catalog or schema names, change the widget values before running.

## Bundle Variables

Open:

```text
databricks.yml
```

The Unity Catalog variables are:

```yaml
catalog_name:
  default: workspace
schema_name:
  default: default
table_name:
  default: exercise_09_customers
```

Change these values if your user does not have permission to write to `workspace.default`.

## Job Configuration

Open:

```text
resources/unity_catalog_table_job.yml
```

The job key is:

```yaml
unity_catalog_table_job:
```

The job passes catalog, schema, and table names as job parameters:

```yaml
parameters:
  - name: catalog_name
    default: ${var.catalog_name}
  - name: schema_name
    default: ${var.schema_name}
  - name: table_name
    default: ${var.table_name}
```

## What The Notebook Does

The notebook:

1. Reads catalog, schema, and table values from widgets.
2. Validates the names.
3. Creates the schema if it does not exist.
4. Filters customer data.
5. Writes a managed Delta table.
6. Reads the table back.

The table name is:

```text
<catalog_name>.<schema_name>.<table_name>
```

## Step 1: Move Into The Exercise Folder

```powershell
cd C:\Users\Sandeep\PycharmProjects\databricks_deployment\exercise_09
```

## Step 2: Validate

```powershell
databricks bundle validate -t dev
```

## Step 3: Deploy

```powershell
databricks bundle deploy -t dev
```

## Step 4: Run

```powershell
databricks bundle run -t dev unity_catalog_table_job
```

## Step 5: Run With A Different Table Name

```powershell
databricks bundle run -t dev --params table_name=exercise_09_customers_test,city=Mumbai,min_id=2 unity_catalog_table_job
```

This writes to a different table for that run.

## What To Check In Databricks

1. Open **Catalog**.
2. Open the catalog used by `catalog_name`.
3. Open the schema used by `schema_name`.
4. Look for the table used by `table_name`.
5. Confirm the rows match the job parameters.

## Common Permission Issue

If the job fails with a catalog or schema permission error, use a catalog and schema where your user has:

1. Permission to use the catalog.
2. Permission to use or create the schema.
3. Permission to create or replace the table.

## Key Idea

Bundle variables define the default Unity Catalog object names.

Job parameters let a run write to a different table without redeploying.

## Clean Up

Delete the table from Catalog Explorer, or run SQL in Databricks:

```sql
DROP TABLE IF EXISTS workspace.default.exercise_09_customers;
DROP TABLE IF EXISTS workspace.default.exercise_09_customers_test;
```

Then remove the deployed bundle resources:

```powershell
databricks bundle destroy -t dev
```
