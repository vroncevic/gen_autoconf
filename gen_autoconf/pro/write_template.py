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
     Created API for write a template content with parameters to a file.
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
__version__ = '2.1.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileChecking):
    '''
        Defined class WriteTemplate with attribute(s) and method(s).
        Created API for write a template content with parameters to a file.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | __pro_dir - project directory.
                | __src_dir - cource directory.
                | __pro_name - project name.
            :methods:
                | __init__ - initial constructor.
                | write - write a template content with parameters to a file.
                | get_pro_dir - getting project directory.
                | get_src_dir - getting source directory.
                | get_pro_name - getting project name.
                | __str__ - dunder method for WriteTemplate.
    '''

    GEN_VERBOSE = 'GEN_AUTOCONF::PRO::WRITE_TEMPLATE'

    def __init__(self, project_name, verbose=False):
        '''
            Initial constructor.

            :param project_name: project name.
            :type project_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:project_name', project_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'init writer')
        self.__pro_dir = '{0}/{1}'.format(getcwd(), project_name)
        self.__src_dir = '{0}/{1}'.format(self.__pro_dir, 'src')
        self.__pro_name = project_name
        if not exists(self.__pro_dir):
            mkdir(self.__pro_dir)
        if not exists(self.__src_dir):
            mkdir(self.__src_dir)

    def get_pro_dir(self):
        '''
            Getting project directory.

            :return: project directory | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__pro_dir

    def get_src_dir(self):
        '''
            Getting source dir.

            :return: source directory | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__src_dir

    def get_pro_name(self):
        '''
            Getting project name.

            :return: project name | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__pro_name

    def write(self, content, module_name, verbose=False):
        '''
            Write a template content with parameters to a file.

            :param content: template content.
            :type content: <str>
            :param module_name: file module name.
            :type module_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:content', content), ('str:module_name', module_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'write templates')
        template, status = Template(content), False
        module_path = '{0}/{1}'.format(self.__pro_dir, module_name)
        with open(module_path, 'w') as module_file:
            module_content = template.substitute(
                {'PRO': '{0}'.format(self.__pro_name)}
            )
            module_file.write(module_content)
            chmod(module_path, 0o666)
            self.check_path(module_path, verbose=verbose)
            self.check_mode('w', verbose=verbose)
            self.check_format(
                module_path, module_path.split('.')[1], verbose=verbose
            )
            if self.is_file_ok():
                status = True
        return status

    def __str__(self):
        '''
            Dunder method for WriteTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            self.__pro_dir, self.__src_dir, self.__pro_name
        )
