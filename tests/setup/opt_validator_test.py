# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenAutoconfBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_autoconf.setup.opt_validator import GenAutoconfBundleOptionsValidator


class TestGenAutoconfBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenAutoconfBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenAutoconfBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenAutoconfBundleOptionsValidator.validate("not_a_mapping")

    def test_validate_invalid_option_type(self) -> None:
        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenAutoconfBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenAutoconfBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenAutoconfBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenAutoconfBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenAutoconfBundleOptionsValidator.is_valid({'info_file': 123}))
