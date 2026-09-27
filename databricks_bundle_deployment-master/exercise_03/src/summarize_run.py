import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print a final summary for the multi-task job run.")
    parser.add_argument("--city", required=True, help="City value used by the job.")
    parser.add_argument("--min_id", required=True, type=int, help="Minimum customer ID used by the job.")
    parser.add_argument("--job_name", required=True, help="Resolved Databricks job name.")
    parser.add_argument("--job_run_id", required=True, help="Resolved Databricks job run ID.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print("Multi-task job summary")
    print(f"job_name: {args.job_name}")
    print(f"job_run_id: {args.job_run_id}")
    print(f"city: {args.city}")
    print(f"min_id: {args.min_id}")
    print("Multi-task job completed successfully.")


if __name__ == "__main__":
    main()
