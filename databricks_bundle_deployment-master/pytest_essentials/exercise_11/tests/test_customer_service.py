from unittest.mock import Mock

from customer_service import fetch_customer


def test_fetch_customer():
    client = Mock()
    client.get_customer.return_value = {
        "id": 101,
        "name": "Sandeep",
    }

    result = fetch_customer(client, 101)

    assert result["name"] == "Sandeep"
    client.get_customer.assert_called_once_with(101)
