from setuptools import find_packages, setup

__package_name__ = "infra"
__package_version = "0.1.0"

setup(
    name=__package_name__,
    version=__package_version,
    author="EmCasa",
    author_email="didier.rda@gmail.com",
    description="infra lib for queroler project",
    url="https://github.com/ro-anderson/backend-PJI240",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "SQLALchemy",
        "PyMySQL"
    ]
)

