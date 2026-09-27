# Databricks notebook source
# MAGIC %md
# MAGIC # Exercise 03 Notebook Version: Task 3
# MAGIC
# MAGIC This notebook represents the final task in the notebook-based multi-task job.
# MAGIC
# MAGIC It should run after `02_process_customers`.

# COMMAND ----------

dbutils.widgets.text("city", "Pune", "City")
dbutils.widgets.text("min_id", "1", "Minimum customer ID")

# COMMAND ----------

city = dbutils.widgets.get("city").strip()
min_id = int(dbutils.widgets.get("min_id"))

print("Multi-task notebook job summary")
print(f"city: {city}")
print(f"min_id: {min_id}")
print("Multi-task notebook job completed successfully.")
