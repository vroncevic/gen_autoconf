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
     Define class WriteTemplate with attribute(s) and method(s).
     Write a template content with parameters to a file.
'''

import sys
from os import getcwd, chmod, mkdir
from os.path import exists
from string import Template

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.5.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(object):
    '''
        Define class WriteTemplate with attribute(s) and method(s).
        Write a template content with parameters to a file.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __pro_dir - Project directory.
                | __src_dir - Source directory.
                | __pro_name - Project name.
            :methods:
                | __init__ - Initial constructor.
                | write - Write a template content with parameters to a file.
                | get_pro_dir - Getting project directory.
                | get_src_dir - getting source directory.
                | get_pro_name - Getting project name.
    '''

    __slots__ = ('VERBOSE', '__pro_dir', '__src_dir', '__pro_name')
    VERBOSE = 'GEN_AUTOCONF::PRO::WRITE_TEMPLATE'

    def __init__(self, project_name, verbose=False):
        '''
            Initial constructor.

            :param project_name: Project name.
            :type project_name: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('str:project_name', project_name)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        verbose_message(WriteTemplate.VERBOSE, verbose, 'init writer')
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

            :exceptions: None
        '''
        return self.__pro_dir

    def get_src_dir(self):
        '''
            Getting project name.

            :exceptions: None
        '''
        return self.__src_dir

    def get_pro_name(self):
        '''
            Getting project name.

            :exceptions: None
        '''
        return self.__pro_name

    def write(self, content, module_name, verbose=False):
        '''
            Write a template content with parameters to a file.

            :param content: Template content.
            :type content: <str>
            :param module_name: File module name.
            :type module_name: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('str:content', content), ('str:module_name', module_name)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        verbose_message(WriteTemplate.VERBOSE, verbose, 'write templates')
        template, status = Template(content), False
        module_path = '{0}/{1}'.format(self.__pro_dir, module_name)
        with open(module_path, 'w') as module_file:
            module_content = template.substitute(
                {'PRO': '{0}'.format(self.__pro_name)}
            )
            module_file.write(module_content)
            chmod(module_path, 0o666)
            status = True
        return True if status else False
