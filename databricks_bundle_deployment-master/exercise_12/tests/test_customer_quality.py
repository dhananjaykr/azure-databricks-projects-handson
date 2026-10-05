import pytest

from customer_quality import filter_customer_rows, validate_inputs


def test_filter_customer_rows_keeps_matching_city_and_minimum_id() -> None:
    assert filter_customer_rows("Pune", 2) == [
        (5, "Riya", "Pune"),
    ]


def test_filter_customer_rows_strips_city_whitespace() -> None:
    assert filter_customer_rows(" Pune ", 1) == [
        (1, "Amit", "Pune"),
        (5, "Riya", "Pune"),
    ]


def test_validate_inputs_rejects_empty_city() -> None:
    with pytest.raises(ValueError, match="city must not be empty"):
        validate_inputs("   ", 1)


def test_validate_inputs_rejects_min_id_less_than_one() -> None:
    with pytest.raises(ValueError, match="min_id must be greater than or equal to 1"):
        validate_inputs("Pune", 0)
