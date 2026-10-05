import pytest

from order_pipeline.config import get_catalog


@pytest.mark.parametrize(
    "environment,expected",
    [
        ("dev", "dev_catalog"),
        ("test", "test_catalog"),
        ("prod", "prod_catalog"),
    ],
)
def test_get_catalog(environment, expected):
    assert get_catalog(environment) == expected


def test_get_catalog_rejects_unknown_environment():
    with pytest.raises(ValueError, match="Unsupported environment: qa"):
        get_catalog("qa")
