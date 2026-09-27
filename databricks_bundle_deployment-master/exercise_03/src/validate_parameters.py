import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate job parameters before processing.")
    parser.add_argument("--city", required=True, help="City value to keep in the output.")
    parser.add_argument("--min_id", required=True, type=int, help="Minimum customer ID to keep.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.city.strip():
        raise ValueError("city must not be empty")

    if args.min_id < 1:
        raise ValueError("min_id must be greater than or equal to 1")

    print("Parameter validation completed successfully.")
    print(f"city: {args.city}")
    print(f"min_id: {args.min_id}")


if __name__ == "__main__":
    main()
