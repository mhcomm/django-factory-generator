#!/usr/bin/env python
import os

from setuptools import find_packages, setup

from factory_generator import VERSION

README = os.path.join(os.path.dirname(__file__), "README.rst")

# When running tests using tox, README.md is not found
try:
    with open(README) as file:
        long_description = file.read()
except Exception:
    long_description = ""


setup(
    name="mh_django_factory_generator",
    version=VERSION,
    description="Generate Model Factory (factory_boy) for each model of your Django app (Fork)",
    long_description=long_description,
    url="https://github.com/mhcomm/django-factory-generator",
    author="Charles TISSIER",
    author_email="charles@vingtcinq.io",
    maintainer="Jonathan LAJUS",
    maintainer_email="lajus@crans.org",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.9",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.3",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="python django factory_boy test",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "isort",
    ],
)
