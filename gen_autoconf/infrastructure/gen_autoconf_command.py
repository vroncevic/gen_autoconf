# -*- coding: UTF-8 -*-

'''
Module
    gen_autoconf_command.py
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
    Defines GenAutoconfCommand class implementing ICLICommand strategy.
'''

from typing import Any, override
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.option.command_option import CommandOption
from gen_autoconf.infrastructure.icli_command import ICLICommand
from gen_autoconf.domain.ports.iservice import IService

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_autoconf'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_autoconf/blob/dev/LICENSE'
__version__: str = '2.7.6'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class GenAutoconfCommand(ICLICommand):
    '''
        CLI subcommand for generating autoconf configuration files.

        It defines:

            :attributes: None.
            :methods:
                | name - Returns the command name key.
                | help_text - Returns the command help text.
                | options - Returns the list of command options.
                | execute - Executes the subcommand.
                | __str__ - Returns the GenAutoconfCommand as string representation.
    '''

    @property
    @override
    def name(self) -> str:
        '''
            Returns the command name key.

            :return: The command name key.
            :rtype: <str>
            :exceptions: None.
        '''
        return "create"

    @property
    @override
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: The command help text.
            :rtype: <str>
            :exceptions: None.
        '''
        return "Generate autoconf project files"

    @property
    @override
    def options(self) -> list[CommandOption]:
        '''
            Returns the command options.

            :return: List of command options.
            :rtype: <list[CommandOption]>
            :exceptions: None.
        '''
        return [
            CommandOption(
                name="--name",
                help_text="Autoconf project name",
                default="mytool",
                required=True
            ),
            CommandOption(
                name="--output",
                help_text="Path to the output directory",
                default="./",
                required=True
            )
        ]

    @override
    def execute(self, params: dict[str, Any], service: IService) -> dict[str, Any]:
        '''
            Executes the subcommand.

            :param params: Subcommand parameters from CLI parser.
            :type params: <dict[str, Any]>
            :param service: Command orchestrator service instance.
            :type service: <IService>
            :return: The result of the subcommand execution.
            :rtype: <dict[str, Any]>
            :exceptions: None.
        '''
        return service.execute(params=params)

    @override
    def __str__(self) -> str:
        '''
            Returns the GenAutoconfCommand as string representation.

            :return: The GenAutoconfCommand as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
