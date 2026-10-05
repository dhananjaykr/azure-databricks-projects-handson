from setuptools import find_packages, setup


setup(
    name="customer_wheel_job",
    version="0.0.1",
    description="Exercise 11 Databricks bundle wheel package",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "main=customer_wheel_job.main:main",
        ],
    },
)
