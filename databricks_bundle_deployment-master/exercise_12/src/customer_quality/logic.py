CUSTOMER_ROWS = [
    (1, "Amit", "Pune"),
    (2, "Neha", "Mumbai"),
    (3, "John", "New York"),
    (4, "Sara", "London"),
    (5, "Riya", "Pune"),
]


def validate_inputs(city: str, min_id: int) -> tuple[str, int]:
    cleaned_city = city.strip()

    if not cleaned_city:
        raise ValueError("city must not be empty")

    if min_id < 1:
        raise ValueError("min_id must be greater than or equal to 1")

    return cleaned_city, min_id


def filter_customer_rows(city: str, min_id: int) -> list[tuple[int, str, str]]:
    cleaned_city, minimum_id = validate_inputs(city, min_id)
    return [
        row
        for row in CUSTOMER_ROWS
        if row[2] == cleaned_city and row[0] >= minimum_id
    ]
