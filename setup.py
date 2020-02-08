#!/usr/bin/env python

from setuptools import setup

setup(
    name="softxperience-pushover",
    version="1.0",
    description="Comprehensive bindings and command line utility for the "
    "Pushover notification service",
    long_description=open("README.rst").read()
    + "\n"
    + open("AUTHORS.rst").read()
    + "\n"
    + open("CHANGES.rst").read(),
    url="https://github.com/SoftXperience/python-pushover",
    author="Marcus Terasa",
    author_email="info@softxperience.com",
    py_modules=["pushover", "cli"],
    entry_points={"console_scripts": ["pushover = cli:main"]},
    install_requires=["requests>=1.0"],
    use_2to3=True,
    license="GNU GPLv3",
)
