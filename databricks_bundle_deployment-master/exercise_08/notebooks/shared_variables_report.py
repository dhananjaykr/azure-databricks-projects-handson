# Databricks notebook source
# MAGIC %md
# MAGIC # Exercise 08 Notebook Demo Version
# MAGIC
# MAGIC This notebook demonstrates the report before bundle variables are used.

# COMMAND ----------

dbutils.widgets.text("report_title", "Customer city report", "Report title")
dbutils.widgets.text("report_owner", "training-team", "Report owner")
dbutils.widgets.text("environment_label", "manual_ui", "Environment")
dbutils.widgets.text("city", "Pune", "City")
dbutils.widgets.text("min_id", "1", "Minimum customer ID")

# COMMAND ----------

from pyspark.sql import functions as F

report_title = dbutils.widgets.get("report_title")
report_owner = dbutils.widgets.get("report_owner")
environment_label = dbutils.widgets.get("environment_label")
city = dbutils.widgets.get("city").strip()
min_id = int(dbutils.widgets.get("min_id"))

print("Report configuration")
print(f"report_title: {report_title}")
print(f"report_owner: {report_owner}")
print(f"environment_label: {environment_label}")
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

display(filtered_df)
print(f"Total matching records: {filtered_df.count()}")
print("Manual shared variables notebook completed successfully.")
