# -*- coding: utf-8 -*-

"""
file: unittest_baseclass.py

Python 2/3 unittest compatibility class
"""

import unittest
import sys

MAJOR_PY_VERSION = sys.version_info[0]

# Unicode test
UNICODE_TYPE = str
if MAJOR_PY_VERSION == 2:
    UNICODE_TYPE = unicode


class UnittestPythonCompatibility(unittest.TestCase):

    def assertItemsEqual(self, expected_seq, actual_seq, msg=None):
        """
        Universal assertItemsEqual method.

        Python 2.x has assertItemsEqual but it is assertCountEqual in 3.x.
        """

        if MAJOR_PY_VERSION == 2:
            return super(UnittestPythonCompatibility, self).assertItemsEqual(expected_seq, actual_seq, msg=msg)
        return super(UnittestPythonCompatibility, self).assertCountEqual(expected_seq, actual_seq, msg=msg)

    def assertViewEqual(self, expected_seq, actual_seq, msg=None):
        """
        Test equality in items even if they are 'view' based
        """

        return all([t in expected_seq for t in actual_seq]) and all([t in actual_seq for t in expected_seq])
