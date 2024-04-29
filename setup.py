import os

from setuptools import setup


def rel(*xs):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *xs)


with open(rel("watchdog_gevent", "__init__.py"), "r") as f:
    version_marker = "__version__ = "
    for line in f:
        if line.startswith(version_marker):
            _, version = line.split(version_marker)
            version = version.strip().strip('"')
            break
    else:
        raise RuntimeError("Version marker not found.")


setup(
    name="watchdog_gevent",
    version=version,
    description="A gevent-based observer for watchdog.",
    long_description="Visit https://github.com/Bogdanp/watchdog_gevent for more information.",
    packages=[
        "watchdog_gevent",
    ],
    install_requires=[
        "gevent>=1.1",
        "watchdog>=4.0",
    ],
    extras_require={
        "dev": [
            "bumpversion",
            "flake8",
            "flake8-quotes",
            "pytest",
            "pytest-cov",
            "twine",
        ]
    },
    include_package_data=True,
    author="Bogdan Popa",
    author_email="bogdan@defn.io",
)
