# Databricks notebook source
# MAGIC %md
# MAGIC # Exercise 06 Notebook Demo Version
# MAGIC
# MAGIC This notebook demonstrates the job logic before showing target-specific bundle deployment.

# COMMAND ----------

dbutils.widgets.text("target_label", "manual_ui", "Target label")
dbutils.widgets.text("city", "Pune", "City")
dbutils.widgets.text("min_id", "1", "Minimum customer ID")

# COMMAND ----------

from pyspark.sql import functions as F

target_label = dbutils.widgets.get("target_label").strip()
city = dbutils.widgets.get("city").strip()
min_id = int(dbutils.widgets.get("min_id"))

if not target_label:
    raise ValueError("target_label must not be empty")

if not city:
    raise ValueError("city must not be empty")

if min_id < 1:
    raise ValueError("min_id must be greater than or equal to 1")

print("Notebook parameters")
print(f"target_label: {target_label}")
print(f"city: {city}")
print(f"min_id: {min_id}")

# COMMAND ----------

data = [
    (1, "Amit", "Pune"),
    (2, "Neha", "Mumbai"),
    (3, "John", "New York"),
    (4, "Sara", "London"),
    (5, "Riya", "Pune"),
]

columns = ["id", "name", "city"]

df = spark.createDataFrame(data, columns)
filtered_df = df.filter((F.col("city") == city) & (F.col("id") >= min_id))

# COMMAND ----------

print("Targeted customer report")
display(filtered_df)

# COMMAND ----------

print(f"Total matching records: {filtered_df.count()}")
print("Manual notebook demo completed successfully.")
