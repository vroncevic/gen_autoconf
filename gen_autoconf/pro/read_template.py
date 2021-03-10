# -*- coding: UTF-8 -*-

'''
 Module
     read_template.py
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
     Define class ReadTemplate with attribute(s) and method(s).
     Read a templates and return a string representations.
'''

import sys
from os.path import isdir

try:
    from pathlib import Path
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
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
__version__ = '1.6.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileChecking):
    '''
        Define class ReadTemplate with attribute(s) and method(s).
        Read a template and return a string representation.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __TEMPLATE_DIR - Prefix path to templates.
                | __template_dir - Absolute template dir.
            :methods:
                | __init__ - Initial constructor.
                | get_template_dir - Getter for template dir path.
                | read - Read a template and return a content or None.
    '''

    __slots__ = ('VERBOSE', '__TEMPLATE_DIR', '__template_dir')
    VERBOSE = 'GEN_AUTOCONF::PRO::READ_TEMPLATE'
    __TEMPLATE_DIR = '/../conf/template/'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(ReadTemplate.VERBOSE, verbose, 'init reader')
        FileChecking.__init__(self, verbose=verbose)
        current_dir = Path(__file__).parent
        template_dir = '{0}{1}'.format(
            current_dir, ReadTemplate.__TEMPLATE_DIR
        )
        check_template_dir = isdir(template_dir)
        if check_template_dir:
            self.__template_dir = template_dir
        else:
            self.__template_dir = None

    def get_template_dir(self):
        '''
            Getter for template dir path.

            :return: Template dir path.
            :rtype: <str>
            :exceptions: None
        '''
        return self.__template_dir

    def read(self, template, verbose=False):
        '''
            Read a template and return a content.

            :param template: File name.
            :type template: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Template content | None.
            :rtype: <str> | <NoneType>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:template', template)])
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        module_content, template_file = None, None
        template_file = '{0}{1}'.format(self.__template_dir, template)
        self.check_path(file_path=template_file, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=template_file, file_format='template', verbose=verbose
        )
        if self.is_file_ok():
            with open(template_file, 'r') as template:
                module_content = template.read()
        return module_content
