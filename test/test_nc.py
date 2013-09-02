#!/usr/bin/env python
"""
Unittests for csvnc module

"""

import os
import pytest
from csvnc import csvnc


class TestCsvnc(object):
    def test_generated_file_should_have_extention_nc(self):
        data_file = 'data.csv'
        assert 'data.nc' == csvnc.new_name(data_file)

