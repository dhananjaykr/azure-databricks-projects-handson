from pyspark.sql import SparkSession


def main() -> None:
    spark = SparkSession.builder.getOrCreate()

    data = [
        (1, "Amit", "Pune"),
        (2, "Neha", "Mumbai"),
        (3, "John", "New York"),
        (4, "Sara", "London"),
    ]
    columns = ["id", "name", "city"]
    df = spark.createDataFrame(data, columns)

    print("Customer Data")
    df.show()

    print(f"Total records: {df.count()}")

    print("Job completed successfully.")


if __name__ == "__main__":
    main()
