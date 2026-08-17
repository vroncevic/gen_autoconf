# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenAutoconfBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_autoconf.setup.keys import GenAutoconfBundleKeys


class TestGenAutoconfBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenAutoconfBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenAutoconfBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenAutoconfBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenAutoconfBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenAutoconfBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenAutoconfBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenAutoconfBundleKeys.OPTION_INFO_FILE, opts)
