# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2020 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class GenAutoconf with attribute(s) and method(s).
    Loads base information, creates a CLI interface, and runs operations.
'''

import sys
from typing import Any, List, Dict
from os.path import exists, dirname, realpath
from os import getcwd
from argparse import Namespace

try:
    from ats_utilities.splash import Splash
    from ats_utilities.logging import ATSLogger
    from ats_utilities.cli import ATSCli
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_autoconf.pro import GenPro
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_autoconf'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_autoconf/blob/dev/LICENSE'
__version__ = '2.7.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenAutoconf(ATSCli):
    '''
        Defines class GenAutoconf with attribute(s) and method(s).
        Loads base information, creates a CLI interface, and runs operations.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _CONFIG - Configuration file path.
                | _LOG - Tool log file path.
                | _LOGO - Logo for splash screen.
                | _OPS - List of tool options.
                | _logger - Logger object API.
            :methods:
                | __init__ - Initials GenAutoconf constructor.
                | process - Processes and runs tool operations.
    '''

    _GEN_VERBOSE: str = 'GEN_AUTOCONF'
    _CONFIG: str = '/conf/gen_autoconf.cfg'
    _LOG: str = '/log/gen_autoconf.log'
    _LOGO: str = '/conf/gen_autoconf.logo'
    _OPS: List[str] = ['-n', '--name', '-v', '--verbose']

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials GenAutoconf constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        current_dir: str = dirname(realpath(__file__))
        gen_autoconf_property: Dict[str, str | bool] = {
            'ats_organization': 'vroncevic',
            'ats_repository': f'{self._GEN_VERBOSE.lower()}',
            'ats_name': f'{self._GEN_VERBOSE.lower()}',
            'ats_logo_path': f'{current_dir}{self._LOGO}',
            'ats_use_github_infrastructure': True
        }
        Splash(gen_autoconf_property, verbose)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(base_info, verbose)
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} init tool info']
        )
        self._logger: ATSLogger = ATSLogger(
            self._GEN_VERBOSE.lower(), True, None, True, verbose
        )
        if self.is_operational():
            self.add_new_option(
                self._OPS[0], self._OPS[1], dest='name',
                help='generate project (provide name)'
            )
            self.add_new_option(
                self._OPS[2], self._OPS[3],
                action='store_true', default=False,
                help='activate verbose mode for generation'
            )

    def process(self, verbose: bool = False) -> bool:
        '''
            Processes and runs operations.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: None
        '''
        status: bool = False
        if self.is_operational():
            try:
                args: Any | Namespace = self.parse_args(sys.argv)
                if not bool(getattr(args, "name")):
                    error_message(
                        [f'{self._GEN_VERBOSE.lower()} missing name argument']
                    )
                    return status
                if exists(f'{getcwd()}/{str(getattr(args, "name"))}'):
                    error_message([
                        f'{self._GEN_VERBOSE.lower()}',
                        f'project with name [{getattr(args, "name")}] exists'
                    ])
                    return status
                gen: GenPro = GenPro(getattr(args, 'verbose') or verbose)
                try:
                    print(
                        " ".join([
                            f'[{self._GEN_VERBOSE.lower()}]',
                            'gen autoconf project skeleton',
                            str(getattr(args, "name"))
                        ])
                    )
                    status = gen.gen_project(
                        f'{getattr(args, "name")}',
                        getattr(args, 'verbose') or verbose
                    )
                except (ATSTypeError, ATSValueError) as e:
                    error_message([f'{self._GEN_VERBOSE.lower()} {str(e)}'])
                    self._logger.write_log(f'{str(e)}', self._logger.ATS_ERROR)
                if status:
                    success_message([f'{self._GEN_VERBOSE.lower()} done\n'])
                    self._logger.write_log(
                        f'generation {getattr(args, "name")} done',
                        self._logger.ATS_INFO
                    )
                else:
                    error_message([f'{self._GEN_VERBOSE.lower()} failed'])
                    self._logger.write_log(
                        'generation failed', self._logger.ATS_ERROR
                    )
            except SystemExit:
                error_message(
                    [f'{self._GEN_VERBOSE.lower()} expected argument -n']
                )
                return status
        else:
            error_message(
                [f'{self._GEN_VERBOSE.lower()} tool is not operational']
            )
            self._logger.write_log(
                'tool is not operational', self._logger.ATS_ERROR
            )
        return status
