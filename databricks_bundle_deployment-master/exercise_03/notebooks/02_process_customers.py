# Databricks notebook source
# MAGIC %md
# MAGIC # Exercise 03 Notebook Version: Task 2
# MAGIC
# MAGIC This notebook represents the second task in the notebook-based multi-task job.
# MAGIC
# MAGIC It should run after `01_validate_parameters`.

# COMMAND ----------

dbutils.widgets.text("city", "Pune", "City")
dbutils.widgets.text("min_id", "1", "Minimum customer ID")

# COMMAND ----------

from pyspark.sql import functions as F

city = dbutils.widgets.get("city").strip()
min_id = int(dbutils.widgets.get("min_id"))

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

print("Processing customer data")
print(f"city: {city}")
print(f"min_id: {min_id}")
display(filtered_df)

# COMMAND ----------

print(f"Total matching records: {filtered_df.count()}")
print("Customer processing notebook completed successfully.")
