# -*- coding: UTF-8 -*-

'''
Module
    test_service.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_autoconf is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_autoconf is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Unit tests for application service (Service).
'''

import unittest
from unittest.mock import MagicMock
from typing import Any, override
from gen_autoconf.domain.ports.iservice import IService
from gen_autoconf.domain.ports.isubprocessor import ISubProcessor
from gen_autoconf.application.service import Service

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_autoconf'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_autoconf/blob/dev/LICENSE'
__version__ = '2.7.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class DummyService(IService):
    '''
        Dummy service implementing IService for coverage.
    '''

    @override
    def execute(self, params: dict[str, Any]) -> dict[str, Any]:
        return super().execute(params)

    @override
    def is_initialized(self) -> bool:
        return super().is_initialized()


class DummySubProcessor(ISubProcessor):
    '''
        Dummy subprocessor implementing ISubProcessor for coverage.
    '''

    @override
    def run(self, command: dict[str, Any]) -> dict[str, Any]:
        return super().run(command)

    @override
    def is_initialized(self) -> bool:
        return super().is_initialized()

    @override
    def __str__(self) -> str:
        return super().__str__()


class TestService(unittest.TestCase):
    '''
        Defines application service unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_init_success - Tests successful service initialization.
                | test_init_failure - Tests initialization failure with None subprocessor.
                | test_execute - Tests execute delegates to subprocessor.
                | test_is_initialized - Tests is_initialized delegates to subprocessor.
                | test_str_repr - Tests service string representation.
    '''

    def test_init_success(self) -> None:
        '''
            Tests successful service initialization.
        '''
        mock_sub: MagicMock = MagicMock(spec=ISubProcessor)
        service: Service = Service(mock_sub)
        self.assertEqual(service._subprocessor, mock_sub)

    def test_init_failure(self) -> None:
        '''
            Tests initialization fails when subprocessor is None.
        '''
        with self.assertRaises(ValueError) as ctx:
            Service(None)
        self.assertEqual(str(ctx.exception), 'subprocessor must be provided.')

    def test_execute(self) -> None:
        '''
            Tests execute delegates run and returns parameters from subprocessor.
        '''
        mock_sub: MagicMock = MagicMock(spec=ISubProcessor)
        expected_res: dict = {"returncode": 0, "stdout": "ok"}
        mock_sub.run.return_value = expected_res

        service: Service = Service(mock_sub)
        params: dict = {"name": "test"}
        res: dict = service.execute(params)

        mock_sub.run.assert_called_once_with(params)
        self.assertEqual(res, expected_res)

    def test_is_initialized(self) -> None:
        '''
            Tests is_initialized delegates check to subprocessor.
        '''
        mock_sub: MagicMock = MagicMock(spec=ISubProcessor)
        
        service: Service = Service(mock_sub)
        
        mock_sub.is_initialized.return_value = True
        self.assertTrue(service.is_initialized())
        
        mock_sub.is_initialized.return_value = False
        self.assertFalse(service.is_initialized())

    def test_str_repr(self) -> None:
        '''
            Tests string representation of Service.
        '''
        mock_sub: MagicMock = MagicMock(spec=ISubProcessor)
        service: Service = Service(mock_sub)
        
        service_str: str = str(service)
        self.assertIsNotNone(service_str)
        self.assertIsInstance(service_str, str)
        self.assertNotEqual(service_str, "")

    def test_iservice_interface(self) -> None:
        '''
            Tests abstract IService interface default implementations.
        '''
        dummy: DummyService = DummyService()
        self.assertIsNone(dummy.execute({}))
        self.assertIsNone(dummy.is_initialized())

    def test_isubprocessor_interface(self) -> None:
        '''
            Tests abstract ISubProcessor interface default implementations.
        '''
        dummy: DummySubProcessor = DummySubProcessor()
        self.assertIsNone(dummy.run({}))
        self.assertIsNone(dummy.is_initialized())
        self.assertIsNone(dummy.__str__())
