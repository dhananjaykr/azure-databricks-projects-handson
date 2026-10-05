# Databricks notebook source
# MAGIC %md
# MAGIC # Exercise 07 Bundle Workspace Path Inspector
# MAGIC
# MAGIC This notebook prints bundle path substitutions passed as job parameters.

# COMMAND ----------

dbutils.widgets.text("bundle_name", "", "Bundle name")
dbutils.widgets.text("bundle_target", "", "Bundle target")
dbutils.widgets.text("workspace_root_path", "", "Workspace root path")
dbutils.widgets.text("workspace_file_path", "", "Workspace file path")

# COMMAND ----------

bundle_name = dbutils.widgets.get("bundle_name")
bundle_target = dbutils.widgets.get("bundle_target")
workspace_root_path = dbutils.widgets.get("workspace_root_path")
workspace_file_path = dbutils.widgets.get("workspace_file_path")

print("Workspace path context")
print(f"bundle_name: {bundle_name}")
print(f"bundle_target: {bundle_target}")
print(f"workspace_root_path: {workspace_root_path}")
print(f"workspace_file_path: {workspace_file_path}")

# COMMAND ----------

path_rows = [
    ("bundle_name", bundle_name),
    ("bundle_target", bundle_target),
    ("workspace_root_path", workspace_root_path),
    ("workspace_file_path", workspace_file_path),
]

display(spark.createDataFrame(path_rows, ["name", "value"]))
