#!/usr/bin/env python

import os
from setuptools import setup

install_requires = [
    'cassandra-driver'
]

name = 'sentry-cassandra-nodestore'
version = '1.2.0'
with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name=name,
    version=version,
    author='Lumanox',
    author_email='opensource@lumanox.com',
    description='A Sentry extension to add Cassandra as a NodeStore backend.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='BSD-style license',
    zip_safe=False,
    include_package_data=True,
    install_requires = [
        'cassandra-driver',
    ],
    packages=[
        'sentry-cassandra-nodestore',
    ],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
