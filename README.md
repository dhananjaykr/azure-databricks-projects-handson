End-to-End Retail Data Engineering Pipeline – AWS Glue | PySpark | Snowflake
🎯 Overview

This project demonstrates an enterprise-grade data engineering pipeline for an e-commerce retail platform.
It processes real-time and batch data from multiple systems such as Kafka, MQ, MongoDB, FTP, and SAP (Article & Inventory) into an analytics-ready Snowflake warehouse.

🧩 Tech Stack

Programming: Python, SQL

Data Processing: PySpark on AWS Glue

Data Storage: AWS S3, Snowflake

Orchestration: Apache Airflow

Cloud Services: AWS EMR, Lambda, IAM, CloudWatch

BI Integration: Tableau, Power BI

🚀 Data Flow

Ingestion: Real-time (Kafka, MQ) and batch data ingested into AWS S3

Transformation: AWS Glue (PySpark) processes and validates 100GB+ SAP & 50GB daily transactional data

Storage: Transformed data loaded into Snowflake for analytics

Orchestration: Airflow automates workflows with alerts and dependency control

Visualization: Tableau dashboards consume curated Snowflake tables

⚡ Optimization Highlights

Optimized PySpark jobs on EMR cluster with broadcast joins and dynamic partitioning

Reduced Glue job runtime by 25%

Automated SLA monitoring via CloudWatch

📊 Project Structure
📂 retail_data_pipeline_aws_glue_pyspark_snowflake
 ┣ 📁 scripts/
 ┣ 📁 airflow_dags/
 ┣ 📁 glue_jobs/
 ┣ 📁 sql_queries/
 ┣ 📁 docs/
 ┗ 📄 README.md

🧑‍💻 Author

Dhananjay Kumar
Data Engineer | AWS Glue | PySpark | Snowflake | Airflow
