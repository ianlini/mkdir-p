#!/usr/bin/env python
from setuptools import setup


description = ("Python 2 and 3 compatible POSIX mkdir -p.")
long_description = ("See `github <https://github.com/ianlini/mkdir-p>`_ "
                    "for more information.")

setup(
    name='mkdir-p',
    version="0.1.0",
    description=description,
    long_description=long_description,
    author='ianlini',
    url='https://github.com/ianlini/mkdir-p',
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    packages=[
        'mkdir_p',
    ],
    package_dir={
        'mkdir_p': 'mkdir_p',
    },
)
