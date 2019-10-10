#! /usr/bin/env python
"""
utils.py unit tests

Created by Dan McGonigle, 10/09/2019
"""
from unittest import TestCase
from utils import *

class UtilsTest(TestCase):
    """A set of unit tests for the functions in utils.py."""
    def setUp(self):
        """Set up the testing environment for various tests."""
        self.mixedlist = ["string", 4.5, TestCase]
        self.emptylist = []
        self.numericlist = [5.3, 2.1, 44, -99]
        self.stringlist = ["a", "bc", "123"]
        self.intlist = [5, 2, -0]
        self.floatlist = [4.4, -1.1, 0.8]

    def test_listtype(self):
        """Ensure that the listtype returns the correct type for each type of list."""

        #   
        self.assertEqual(listtype(self.mixedlist), "mixed"), "Failed listtype mixedlist test"
        self.assertIsNone(listtype(self.emptylist)), "Failed listtype emptylist test"
        self.assertEqual(listtype(self.numericlist), float), "Failed listtype numericlist test"
        self.assertEqual(listtype(self.stringlist), str), "Failed listtype stringlist test"
        self.assertEqual(listtype(self.intlist), float), "Failed listtype intlist test"
        self.assertEqual(listtype(self.floatlist), float), "Failed listtype floatlist test"
