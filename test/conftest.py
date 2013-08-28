#!/usr/bin/env python
"""
Fixtures for unittests
"""

import os
import tempfile
import pytest


@pytest.fixture()
def cleandir():
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)

