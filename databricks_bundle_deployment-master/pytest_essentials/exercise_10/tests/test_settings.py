from settings import get_environment


def test_environment_defaults_to_dev(monkeypatch):
    monkeypatch.delenv("APP_ENV", raising=False)

    assert get_environment() == "dev"


def test_environment_can_be_set(monkeypatch):
    monkeypatch.setenv("APP_ENV", "test")

    assert get_environment() == "test"
