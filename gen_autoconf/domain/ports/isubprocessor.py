# -*- coding: UTF-8 -*-

'''
Module
    isubprocessor.py
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
    Defines abstract interface for sub-process execution.
'''

from abc import ABC, abstractmethod
from typing import Any

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_autoconf'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_autoconf/blob/dev/LICENSE'
__version__: str = '1.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class ISubProcessor(ABC):
    '''
        Abstract interface for sub-process execution.

        It defines:

            :attributes: None.
            :methods:
                | run - Executes a sub-process.
                | is_initialized - Checks if the subprocessor is initialized.
                | __str__ - Returns the SubProcessor as string representation.
    '''

    @abstractmethod
    def run(self, command: dict[str, Any]) -> dict[str, Any]:
        '''
            Runs a sub-process.

            :param command: The command to execute.
            :type command: <dict[str, Any]>
            :return: The result of the sub-process execution.
            :rtype: <dict[str, Any]>
            :exceptions: None.   
        '''
        pass

    @abstractmethod
    def is_initialized(self) -> bool:
        '''
            Checks if the subprocessor is initialized.

            :return: True if the subprocessor is initialized, False otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        pass

    @abstractmethod
    def __str__(self) -> str:
        '''
            Returns the SubProcessor as string representation.

            :return: The SubProcessor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        pass
