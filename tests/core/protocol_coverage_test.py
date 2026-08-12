# -*- coding: UTF-8 -*-

'''
Module
    protocol_coverage_test.py
Info
    Unit tests to cover stubs in protocol definitions (IService and ISubProcessor).
'''

from __future__ import annotations

import unittest

from gen_autoconf.core.service.iservice import IService
from gen_autoconf.core.service.isubprocessor import ISubProcessor


class TestProtocolCoverage(unittest.TestCase):

    def test_iservice_protocol_stubs(self) -> None:
        # Call stubs directly on the Protocol class to cover the 'pass' statements.
        self.assertIsNone(IService.execute(None, params=None))
        self.assertIsNone(IService.is_initialized(None))

    def test_isubprocessor_protocol_stubs(self) -> None:
        # Call stubs directly on the ISubProcessor protocol class.
        self.assertIsNone(ISubProcessor.run(None, params=None))
        self.assertIsNone(ISubProcessor.is_initialized(None))
