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
     Defined class ReadTemplate with attribute(s) and method(s).
     Created API for read a templates and return a string representations.
'''

import sys
from os.path import isdir

try:
    from pathlib import Path
    from ats_utilities.checker import ATSChecker
    from ats_utilities.cooperative import CooperativeMeta
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
__version__ = '2.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileChecking):
    '''
        Defined class ReadTemplate with attribute(s) and method(s).
        Created API for read a templates and return a string representations.
        It defines:

            :attributes:
                | __metaclass__ - setting cooperative metaclasses.
                | GEN_VERBOSE - console text indicator for process-phase.
                | TEMPLATE_DIR - prefix path to templates.
                | __template_dir - absolute template dir.
            :methods:
                | __init__ - initial constructor.
                | get_template_dir - getter for template dir path.
                | read - read a template and return a content or None.
                | __str__ - dunder method for ReadTemplate.
    '''

    __metaclass__ = CooperativeMeta
    GEN_VERBOSE = 'GEN_AUTOCONF::PRO::READ_TEMPLATE'
    TEMPLATE_DIR = '/../conf/template/'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(ReadTemplate.GEN_VERBOSE, verbose, 'init reader')
        current_dir = Path(__file__).parent
        template_dir = '{0}{1}'.format(current_dir, ReadTemplate.TEMPLATE_DIR)
        check_template_dir = isdir(template_dir)
        if check_template_dir:
            self.__template_dir = template_dir
        else:
            self.__template_dir = None

    def get_template_dir(self):
        '''
            Getter for template dir path.

            :return: template dir path.
            :rtype: <str>
            :exceptions: None
        '''
        return self.__template_dir

    def read(self, template_file, verbose=False):
        '''
            Read a template and return a content.

            :param template_file: file name.
            :type template_file: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: template content | None.
            :rtype: <str> | <NoneType>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:template_file', template_file)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        module_content, template_file_path = None, None
        template_file_path = '{0}{1}'.format(
            self.__template_dir, template_file
        )
        self.check_path(file_path=template_file_path, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=template_file_path, file_format='template',
            verbose=verbose
        )
        if self.is_file_ok():
            with open(template_file_path, 'r') as template:
                module_content = template.read()
        return module_content

    def __str__(self):
        '''
            Dunder method for ReadTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            self.__template_dir
        )
