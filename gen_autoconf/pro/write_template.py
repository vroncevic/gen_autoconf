# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
 Copyright
     Copyright (C) 2020 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class WriteTemplate with attribute(s) and method(s).
     Created API for write a templates with parameters.
'''

import sys
from os import getcwd, chmod, mkdir
from os.path import exists
from string import Template

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, https://vroncevic.github.io/gen_autoconf'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_autoconf/blob/dev/LICENSE'
__version__ = '2.2.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileChecking):
    '''
        Defined class WriteTemplate with attribute(s) and method(s).
        Created API for write a templates with parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
            :methods:
                | __init__ - initial constructor.
                | write - write a templates with parameters.
                | __str__ - dunder method for WriteTemplate.
    '''

    GEN_VERBOSE = 'GEN_AUTOCONF::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'init writer')

    def write(self, templates, project_name, verbose=False):
        '''
            Write a templates with parameters.

            :param templates: parameter templates.
            :type templates: <list>
            :param project_name: parameter project name.
            :type project_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('list:templates', templates), ('str:project_name', project_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        statuses = []
        pro_dir = '{0}/{1}/'.format(getcwd(), project_name)
        src_dir = '{0}/{1}/src'.format(getcwd(), project_name)
        status, expected_num_of_modules = False, len(templates)
        if not exists(pro_dir):
            mkdir(pro_dir)
            mkdir(src_dir)
        for template_content in templates:
            print(template_content)
            module_name = list(template_content.keys())[0]
            template = Template(template_content[module_name])
            module_path = '{0}{1}'.format(pro_dir, module_name)
            with open(module_path, 'w') as module_file:
                module_content = template.substitute(
                    {'PRO': '{0}'.format(project_name)}
                )
                module_file.write(module_content)
                chmod(module_path, 0o666)
                self.check_path(module_path, verbose=verbose)
                self.check_mode('w', verbose=verbose)
                if 'makefile'.capitalize() in module_path:
                    self.check_format(
                        module_path, 'makefile', verbose=verbose
                    )
                else:
                    self.check_format(
                        module_path, module_path.split('.')[1],
                        verbose=verbose
                    )
                if self.is_file_ok():
                    statuses.append(True)
                else:
                    statuses.append(False)
        if all(statuses) and len(statuses) == expected_num_of_modules:
            status = True
        return status

    def __str__(self):
        '''
            Dunder method for WriteTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, FileChecking.__str__(self)
        )
