import argparse

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a packaged customer report.")
    parser.add_argument("--city", required=True, help="City value to keep in the output.")
    parser.add_argument("--min_id", required=True, type=int, help="Minimum customer ID to keep.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    city = args.city.strip()
    min_id = args.min_id

    if not city:
        raise ValueError("city must not be empty")

    if min_id < 1:
        raise ValueError("min_id must be greater than or equal to 1")

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
    filtered_df = df.filter((F.col("city") == city) & (F.col("id") >= min_id))

    print("Python wheel task parameters")
    print(f"city: {city}")
    print(f"min_id: {min_id}")

    print("Filtered customer data")
    filtered_df.show()

    print(f"Total matching records: {filtered_df.count()}")
    print("Python wheel job completed successfully.")


if __name__ == "__main__":
    main()
