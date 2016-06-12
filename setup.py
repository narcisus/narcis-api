#!/usr/bin/env python

from distutils.core import setup

setup(
    name='narcis-api',
    version='0.0.1',
    description='The core API module for metadata about build screenshots',
    author='Jared Deckard',
    author_email='jared.deckard@gmail.com',
    url='https://github.com/narcisus/narcis-api',
    packages=['narcis_api', 'narcis_api.models'],
    package_dir={'narcis_api': 'narcis_api'},
)
