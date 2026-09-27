import argparse

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Filter customer data by city and minimum ID.")
    parser.add_argument("--city", required=True, help="City value to keep in the output.")
    parser.add_argument("--min_id", required=True, type=int, help="Minimum customer ID to keep.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    spark = SparkSession.builder.getOrCreate()

    data = [
        (1, "Amit", "Pune"),
        (2, "Neha", "Mumbai"),
        (3, "John", "New York"),
        (4, "Sara", "London"),
        (5, "Riya", "Pune"),
    ]
    columns = ["id", "name", "city"]

    df = spark.createDataFrame(data, columns)
    filtered_df = df.filter((F.col("city") == args.city) & (F.col("id") >= args.min_id))

    print("Processing customer data")
    print(f"city: {args.city}")
    print(f"min_id: {args.min_id}")

    filtered_df.show()

    print(f"Total matching records: {filtered_df.count()}")
    print("Customer processing completed successfully.")


if __name__ == "__main__":
    main()
