import argparse

from pyspark.sql import SparkSession

from customer_quality import filter_customer_rows, validate_inputs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a tested customer quality job.")
    parser.add_argument("--city", required=True, help="City value to keep in the output.")
    parser.add_argument("--min_id", required=True, type=int, help="Minimum customer ID to keep.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    city, min_id = validate_inputs(args.city, args.min_id)

    spark = SparkSession.builder.getOrCreate()
    rows = filter_customer_rows(city, min_id)
    df = spark.createDataFrame(rows, ["id", "name", "city"])

    print("Tested Python file task parameters")
    print(f"city: {city}")
    print(f"min_id: {min_id}")

    print("Filtered customer data")
    df.show()

    print(f"Total matching records: {df.count()}")
    print("Tested Python file job completed successfully.")


if __name__ == "__main__":
    main()
