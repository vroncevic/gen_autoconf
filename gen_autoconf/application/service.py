# -*- coding: UTF-8 -*-

'''
Module
    service.py
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
    Defines application service for file generation.
'''

from typing import Any, override
from gen_autoconf.domain.ports.iservice import IService
from gen_autoconf.domain.ports.isubprocessor import ISubProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_autoconf'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_autoconf/blob/dev/LICENSE'
__version__: str = '2.7.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class Service(IService):
    '''
        Service for orchestrating the file generation process.

        It defines:

            :attributes:
                | _subprocessor - Adapter for subprocessing.
            :methods:
                | execute - Generates and writes user files.
                | is_initialized - Checks if the service component is initialized.
    '''

    def __init__(self, subprocessor: ISubProcessor) -> None:
        '''
            Initializes the Service.

            :param subprocessor: Subprocessor adapter.
            :type subprocessor: <ISubProcessor>
            :exceptions:
                | ValueError: Subprocessor must be provided.
        '''
        if subprocessor is None:
            raise ValueError('subprocessor must be provided.')

        self._subprocessor: ISubProcessor = subprocessor

    @override
    def execute(self, params: dict[str, Any]) -> dict[str, Any]:
        '''
            Generates picom configuration files.

            :param params: Parameters for template formatting.
            :type params: <dict[str, Any]>
            :return: Return code, stdout and stderr messages.
            :return type: <dict[str, Any]>
            :exceptions: None.
        '''
        return self._subprocessor.run(params)

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the service component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._subprocessor.is_initialized()
