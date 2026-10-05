import pytest

from calculator import add


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 20, 30),
        (1, 2, 3),
        (-1, 1, 0),
        (0, 0, 0),
        (100, 200, 300),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_add_1(a, b, expected):
    assert add(a, b) == expected


def test_add_2():
    assert add(10, 10) == 20
