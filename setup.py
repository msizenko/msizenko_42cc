#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='msizenko_42cc',
    version='0.1',
    author="msizenko",
    author_email='msizenko@gmail.com',
    url='',
    packages=find_packages(),
    package_data={'msizenko_42cc': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
