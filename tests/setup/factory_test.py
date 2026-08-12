# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenAutoconfBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_autoconf.setup.bundle import GenAutoconfBundle
from gen_autoconf.setup.factory import GenAutoconfBundleFactory


class TestGenAutoconfBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenAutoconfBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenAutoconfBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_autoconf/infrastructure/config/gen_autoconf.cfg'}
        bundle = GenAutoconfBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenAutoconfBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenAutoconfBundleFactory.create_bundle(options)

