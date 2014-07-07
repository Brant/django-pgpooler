#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

required = [
    'psycopg2',
    'sqlalchemy'
]

setup(
    name='django-pgpooler',
    version='0.1.0',
    description='PostgreSQL Pooling for Django.',
    long_description=open('README.md').read(),
    author='Brant Steen',
    author_email='brant.steen@gmail.com',
    url='https://github.com/Brant/django-pgpooler',
    packages=['django_pgpooler', ],
    install_requires=required,
    license='MIT',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        # 'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
    ),
)
