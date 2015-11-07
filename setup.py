# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def read(*paths):
    """ read files """
    with open(os.path.join(*paths), 'r') as filename:
        return filename.read()


install_requires = read('requirements.txt').splitlines()

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="pypptx",
    version="0.2.1",
    description="Create a pptx from plain text",
    license="MIT",
    author="JuanPablo AJ",
    author_email="jpabloaj@gmail.com",
    packages=find_packages(),
    install_requires=install_requires,
    long_description=long_description,
    url="https://github.com/juanpabloaj/pypptx",
    test_suite="tests",
    entry_points={
        'console_scripts': [
            'pptx=pypptx:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
