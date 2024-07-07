# -*- coding: UTF-8 -*-

'''
Module
    write_template.py
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
    Defines class WriteTemplate with attribute(s) and method(s).
    Creates an API for writing source and build modules.
'''

import sys
from typing import List, Dict, Optional
from os import getcwd, chmod, mkdir
from os.path import exists
from datetime import datetime
from string import Template

try:
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
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


class WriteTemplate(FileCheck):
    '''
        Defines class WriteTemplate with attribute(s) and method(s).
        Creates an API for writing source and build modules.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
            :methods:
                | __init__ - Initials WriteTemplate constructor.
                | write - Writes a templates with parameters.
    '''

    _GEN_VERBOSE: str = 'GEN_AUTOCONF::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials WriteTemplate constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: ATSTypeError
        '''
        super().__init__(verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init writer'])

    def write(
        self,
        templates: List[Dict[str, str]],
        pro_name: Optional[str],
        verbose: bool = False
    ) -> bool:
        '''
            Writes a templates with parameters.

            :param templates: List of templates
            :type templates: <List[Dict[str, str]]>
            :param pro_name: Project name | None
            :type pro_name: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (templates written) | False
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('list:templates', templates), ('str:pro_name', pro_name)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(templates):
            raise ATSValueError('missing templates')
        if not bool(pro_name):
            raise ATSValueError('missing project name')
        all_stat: List[bool] = []
        pro_dir: str = f'{getcwd()}/{pro_name}/'
        src_dir: str = f'{getcwd()}/{pro_name}/src'
        num_of_modules: int = len(templates)
        if not exists(pro_dir):
            mkdir(pro_dir)
            mkdir(src_dir)
        for template_content in templates:
            module_name: str = list(template_content.keys())[0]
            template: Template = Template(template_content[module_name])
            module_path: str = f'{pro_dir}{module_name}'
            with open(module_path, 'w', encoding='utf-8') as module_file:
                module_content: str = template.substitute(
                    {
                        'PRO': f'{pro_name}',
                        'YEAR': f'{datetime.now().year}'
                    }
                )
                module_file.write(module_content)
                chmod(module_path, 0o666)
                self.check_path(module_path, verbose)
                self.check_mode('w', verbose)
                if 'makefile'.capitalize() in module_path:
                    self.check_format(module_path, 'makefile', verbose)
                else:
                    self.check_format(
                        module_path, module_path.split('.')[1], verbose
                    )
                if self.is_file_ok():
                    all_stat.append(True)
                else:
                    all_stat.append(False)
        return all([
            bool(all_stat), all(all_stat), len(all_stat) == num_of_modules
        ])
