#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

__version__ = "0.0.0"

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as history_file:
    history = history_file.read()

install_requirements = [
    "pytest>=3.2",
    "behave==1.2.5",
    "freezegun==0.3.12",
    "pytest-runner>=3",
    "pyfakefs==3.6",
]

setup(
    name="sceptre-test-rig",
    version=__version__,
    description="Sceptre Acceptance Test Rig",
    author_email="sceptre@cloudreach.com",
    license='Apache2',
    url="https://github.com/Sceptre/sceptre-test-rig",
    keywords="sceptre",
    test_suite="tests",
    install_requires=install_requirements,
)
