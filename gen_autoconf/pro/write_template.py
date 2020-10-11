# -*- coding: UTF-8 -*-

"""
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
"""

import sys
from os import getcwd, chmod, mkdir
from os.path import exists
from string import Template
from inspect import stack

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(object):
    """
        Define class WriteTemplate with attribute(s) and method(s).
        Write a template content with parameters to a file.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __pro_dir - Project directory
                | __src_dir - Source directory
                | __pro_name - Project name
            :methods:
                | __init__ - Initial constructor
                | write - Write a template content with parameters to a file
    """

    __slots__ = ('VERBOSE', '__pro_dir', '__src_dir', '__pro_name')
    VERBOSE = 'GEN_AUTOCONF::PRO::WRITE_TEMPLATE'

    def __init__(self, project_name, verbose=False):
        """
            Initial constructor.

            :param project_name: Project name
            :type project_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        pro_name_txt = 'Argument: expected project_name <str> object'
        pro_name_msg = "{0} {1} {2}".format('def', func, pro_name_txt)
        verbose_message(WriteTemplate.VERBOSE, verbose, 'Initial writer')
        if project_name is None or not project_name:
            raise ATSBadCallError(pro_name_msg)
        if not isinstance(project_name, str):
            raise ATSTypeError(pro_name_msg)
        self.__pro_dir = "{0}/{1}".format(getcwd(), project_name)
        self.__src_dir = "{0}/{1}".format(self.__pro_dir, 'src')
        self.__pro_name = project_name
        if not exists(self.__pro_dir):
            mkdir(self.__pro_dir)
        if not exists(self.__src_dir):
            mkdir(self.__src_dir)

    def get_pro_dir(self):
        """
            Getting project directory.

            :exceptions: None
        """
        return self.__pro_dir

    def get_src_dir(self):
        """
            Getting project name.

            :exceptions: None
        """
        return self.__src_dir

    def get_pro_name(self):
        """
            Getting project name.

            :exceptions: None
        """
        return self.__pro_name

    def write(self, content, template_name, verbose=False):
        """
            Write a template content with parameters to a file.

            :param content: Template content
            :type content: <str>
            :param template_name: File name
            :type template_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Boolean status, True (success) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        status, func = False, stack()[0][3]
        content_txt = 'Argument: expected content <str> object'
        content_msg = "{0} {1} {2}".format('def', func, content_txt)
        name_txt = 'Argument: expected template_name <str> object'
        name_msg = "{0} {1} {2}".format('def', func, name_txt)
        if content is None or not content:
            raise ATSBadCallError(content_msg)
        if not isinstance(content, str):
            raise ATSTypeError(content_msg)
        if template_name is None or not template_name:
            raise ATSBadCallError(name_msg)
        if not isinstance(template_name, str):
            raise ATSTypeError(name_msg)
        verbose_message(WriteTemplate.VERBOSE, verbose, 'Write templates')
        template = Template(content)
        template_path = "{0}/{1}".format(self.__pro_dir, template_name)
        with open(template_path, 'w') as module_file:
            module_content = template.substitute(
                {'PRO': "{0}".format(self.__pro_name)}
            )
            module_file.write(module_content)
            chmod(template_path, 0o666)
            status = True
        return True if status else False
