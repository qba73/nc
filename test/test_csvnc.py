#!/usr/bin/env python
"""
Unittests for csvnc module

"""

import pytest
from csvnc import csvnc


class TestCsvnc(object):
    @classmethod
    def setup_class(cls):
        pass
    
    def test_generated_file_should_have_extention_nc(self):
        data_file = 'data.csv'
        assert 'data.nc' == csvnc.new_name(data_file)

    @classmethod
    def teardown_class(cls):
        pass
