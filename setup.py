#!/usr/bin/env python

import os
import sys
from setuptools.command.test import test as TestCommand
import csvnc


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True 

    def run_tests(self):
        # import here, cause outside the
        # eggs aren't imported
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://csvnc.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')



setup(
    name='csvnc',
    version='0.1.0',
    description='Simple csv to nc file format converter.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Jakub Jarosz',
    author_email='jakub.s.jarosz@gmail.com',
    url='https://github.com/qba73/nc',
    packages=[
        'csvnc',
    ],
    package_dir={'csvnc': 'csvnc'},
    include_package_data=True,
    install_requires=[
    ],
    keywords=['netcdf', 'nc', 'gis', 'csv'],
    entry_points={'console_scripts': ['csvnc = csvnc.csvnc:main']},
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Aplha',
        'Intendent Audience :: GIS Technicians',
        'Licence  :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    tests_require=['pytest>=2.3.5'],
    cmdclass = {'test': PyTest}, 
)

