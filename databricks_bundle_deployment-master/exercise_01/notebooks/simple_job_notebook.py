# Databricks notebook source
# MAGIC %md
# MAGIC # Exercise 01 Notebook Version
# MAGIC
# MAGIC This notebook demonstrates the same logic as the bundle Python file job in `src/main.py`.
# MAGIC
# MAGIC Use this notebook first to show the Databricks notebook workflow. The bundle version then shows how the same job is represented with local files and YAML.

# COMMAND ----------

data = [
    (1, "Amit", "Pune"),
    (2, "Neha", "Mumbai"),
    (3, "John", "New York"),
    (4, "Sara", "London"),
]

columns = ["id", "name", "city"]

df = spark.createDataFrame(data, columns)

# COMMAND ----------

print("Customer Data")
display(df)

# COMMAND ----------

print(f"Total records: {df.count()}")
print("Notebook job completed successfully.")
