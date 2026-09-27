# 🚀 Azure Databricks Projects Hands-On & DABs Deployment

[![Databricks](https://img.shields.io/badge/Databricks-Asset_Bundles_(DABs)-FF3621?logo=databricks&logoColor=white)](https://databricks.com/)
[![Azure](https://img.shields.io/badge/Azure-Data_Engineering-0078D4?logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/)
[![PySpark](https://img.shields.io/badge/PySpark-3.x-E25A1C?logo=apachespark&logoColor=white)](https://spark.apache.org/)
[![Snowflake](https://img.shields.io/badge/Snowflake-Data_Warehouse-29B5E8?logo=snowflake&logoColor=white)](https://www.snowflake.com/)

---

## 🎯 Project Overview

This repository showcases enterprise-grade end-to-end data engineering pipelines developed using **Azure Databricks**, **PySpark**, **AWS S3 / ADLS Gen2**, and **Snowflake**. 

It demonstrates modern **Software Engineering best practices for Data Engineering (CI/CD & Infrastructure as Code)** by automating Databricks workflow deployments using **Databricks Asset Bundles (DABs)** and **Databricks CLI** directly from local IDEs (PyCharm / VS Code) to cloud workspaces.

---

## 🧩 Tech Stack & Tools

* **Cloud Data Platform:** Azure Databricks (Free / Community Edition & Enterprise Workspaces)
* **Programming & Frameworks:** Python 3.x, SQL, PySpark (Structured Streaming & Batch API)
* **Deployment & IaC:** Databricks Asset Bundles (DABs), Databricks CLI v0.200+
* **Data Storage & Warehousing:** AWS S3 / Azure Blob Storage, Snowflake Data Warehouse
* **Local Development & Version Control:** PyCharm Professional, Git, GitHub
* **Orchestration:** Databricks Workflows / Multi-Task Jobs

---

## 🏗️ Architecture & Deployment Flow

```text
+---------------------+        +--------------------+        +-------------------------+
|   Local Machine     |        |   Databricks CLI   |        |    Azure Databricks     |
|   (PyCharm IDE)     | -----> |   (DABs Engine)    | -----> |    Workspace & Jobs     |
| Code & databricks.yml|        | Validate & Deploy  |        | Execution / Workflows   |
+---------------------+        +--------------------+        +-------------------------+
                                                                          |
                                                                          v
                                                             +-------------------------+
                                                             |   Target Warehouse      |
                                                             |  (Snowflake / Delta Lake)|
                                                             +-------------------------+
