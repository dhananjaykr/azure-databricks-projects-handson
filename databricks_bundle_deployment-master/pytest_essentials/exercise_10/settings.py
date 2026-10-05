import os


def get_environment():
    return os.getenv("APP_ENV", "dev")
