# Databricks notebook source
# MAGIC %md
# MAGIC # Exercise 07 Notebook Demo Version
# MAGIC
# MAGIC This notebook demonstrates the path values that the bundle version prints automatically.

# COMMAND ----------

dbutils.widgets.text("bundle_name", "manual_ui", "Bundle name")
dbutils.widgets.text("bundle_target", "manual", "Bundle target")
dbutils.widgets.text("workspace_root_path", "/Workspace/Users/<user>/.bundle_training/<bundle>/<target>", "Workspace root path")
dbutils.widgets.text("workspace_file_path", "/Workspace/Users/<user>/.bundle_training/<bundle>/<target>/files", "Workspace file path")

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
