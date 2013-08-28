from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand

import io
import codecs
import os
import os.path
import sys

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())

long_description = read('README.txt', 'CHANGES.txt')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['-v']
        self.test_suite = True

    def run_test(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='csvnc',
    version='0.1.0',
    description='csv to nc converter',
    author=('Jakub Jarosz <jakub.s.jarosz@gmail.com>',),
    author_email='jakub.s.jarosz at gmail.com',
    url='https://github.com/qba73/nc',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    entry_points={'console_scripts': ['csvnc = csvnc.csvnc:main']},
    packages=['csvnc'],
    license='GPL',
    zip_safe=False,
    keywords=['netcdf', 'nc', 'gis', 'csv'],
    classifiers=[
        'Development Status :: 1 - Aplha',
        'Intendent Audience :: GIS Technicians',
        'Licence  :: OSI Approved :: GNU General Pulic Licence (GPL)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ], 
)
