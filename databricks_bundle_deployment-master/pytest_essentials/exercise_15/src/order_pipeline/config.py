CATALOGS = {
    "dev": "dev_catalog",
    "test": "test_catalog",
    "prod": "prod_catalog",
}


def get_catalog(environment):
    if environment not in CATALOGS:
        raise ValueError(f"Unsupported environment: {environment}")

    return CATALOGS[environment]
