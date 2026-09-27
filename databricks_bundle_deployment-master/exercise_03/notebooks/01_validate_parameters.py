# Databricks notebook source
# MAGIC %md
# MAGIC # Exercise 03 Notebook Version: Task 1
# MAGIC
# MAGIC This notebook represents the first task in the notebook-based multi-task job.
# MAGIC
# MAGIC It validates the input parameters before the processing notebook runs.

# COMMAND ----------

dbutils.widgets.text("city", "Pune", "City")
dbutils.widgets.text("min_id", "1", "Minimum customer ID")

# COMMAND ----------

city = dbutils.widgets.get("city").strip()
min_id = int(dbutils.widgets.get("min_id"))

if not city:
    raise ValueError("city must not be empty")

if min_id < 1:
    raise ValueError("min_id must be greater than or equal to 1")

print("Parameter validation completed successfully.")
print(f"city: {city}")
print(f"min_id: {min_id}")
