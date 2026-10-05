# Databricks notebook source
# MAGIC %md
# MAGIC # Exercise 09 Bundle Unity Catalog Table Job
# MAGIC
# MAGIC This notebook is deployed by the bundle.
# MAGIC
# MAGIC It writes and reads a Unity Catalog managed Delta table.

# COMMAND ----------

dbutils.widgets.text("catalog_name", "workspace", "Catalog")
dbutils.widgets.text("schema_name", "default", "Schema")
dbutils.widgets.text("table_name", "exercise_09_customers", "Table")
dbutils.widgets.text("city", "Pune", "City")
dbutils.widgets.text("min_id", "1", "Minimum customer ID")

# COMMAND ----------

import re

from pyspark.sql import functions as F

catalog_name = dbutils.widgets.get("catalog_name").strip()
schema_name = dbutils.widgets.get("schema_name").strip()
table_name = dbutils.widgets.get("table_name").strip()
city = dbutils.widgets.get("city").strip()
min_id = int(dbutils.widgets.get("min_id"))

identifier_pattern = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

for label, value in [
    ("catalog_name", catalog_name),
    ("schema_name", schema_name),
    ("table_name", table_name),
]:
    if not identifier_pattern.match(value):
        raise ValueError(f"{label} must use only letters, numbers, and underscores, and cannot start with a number")

if not city:
    raise ValueError("city must not be empty")

if min_id < 1:
    raise ValueError("min_id must be greater than or equal to 1")

full_table_name = f"`{catalog_name}`.`{schema_name}`.`{table_name}`"

print("Unity Catalog target")
print(f"catalog_name: {catalog_name}")
print(f"schema_name: {schema_name}")
print(f"table_name: {table_name}")
print(f"full_table_name: {catalog_name}.{schema_name}.{table_name}")

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

spark.sql(f"CREATE SCHEMA IF NOT EXISTS `{catalog_name}`.`{schema_name}`")

filtered_df.write.mode("overwrite").format("delta").saveAsTable(full_table_name)

print(f"Wrote table: {catalog_name}.{schema_name}.{table_name}")

# COMMAND ----------

result_df = spark.table(full_table_name)

print("Rows read from Unity Catalog table")
display(result_df)

print(f"Total table records: {result_df.count()}")
print("Unity Catalog bundle notebook job completed successfully.")
