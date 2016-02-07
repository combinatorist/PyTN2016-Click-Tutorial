#!/usr/bin/env python

import sys
from codecs import open
from os import path
from setuptools import setup

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

test_requirements = [
    'mock',
    'pytest',
    'tox',
]

requirements = [
    'click>=6.0',
    'colorama',
] + test_requirements

python2_requirements = [
    'importlib',
    ]

if sys.version_info[0] == 2:
    requirements += python2_requirements

setup(
    name='click_tutorial',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Tutorial for writing command line applications using click.",
    long_description=readme,
    author="Dave Forgac",
    author_email='tylerdave@tylerdave.com',
    url='https://github.com/tylerdave/click_tutorial',
    packages=['click_tutorial'],
    package_data={'click_tutorial': ['data/tutorial_lessons.json']},
    # NOTE: SLIDE 1 - THIS ADDS THE COMMANDS TO THE COMMAND LINE (PER VIRTUAL ENV) - ALL OS'S
    entry_points={
        'console_scripts':[
            'pytn=click_tutorial.cli:cli',
            'hello=click_tutorial.hello:cli',
            'tutorial=click_tutorial.tutorial_runner:cli',
            ],
        },
    install_requires=requirements,
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
