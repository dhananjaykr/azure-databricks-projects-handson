# Databricks notebook source
# MAGIC %md
# MAGIC # Exercise 05 Notebook Demo Version
# MAGIC
# MAGIC This notebook demonstrates the job logic before adding the schedule in the bundle.

# COMMAND ----------

dbutils.widgets.text("city", "Pune", "City")
dbutils.widgets.text("min_id", "1", "Minimum customer ID")

# COMMAND ----------

from datetime import datetime, timezone

from pyspark.sql import functions as F

city = dbutils.widgets.get("city").strip()
min_id = int(dbutils.widgets.get("min_id"))

if not city:
    raise ValueError("city must not be empty")

if min_id < 1:
    raise ValueError("min_id must be greater than or equal to 1")

print("Notebook parameters")
print(f"city: {city}")
print(f"min_id: {min_id}")
print(f"run_utc: {datetime.now(timezone.utc).isoformat()}")

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

print("Scheduled customer report")
display(filtered_df)

# COMMAND ----------

print(f"Total matching records: {filtered_df.count()}")
print("Scheduled notebook demo completed successfully.")
