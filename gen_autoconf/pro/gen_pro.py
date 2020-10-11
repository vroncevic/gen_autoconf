# -*- coding: UTF-8 -*-

"""
 Module
     gen_pro.py
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
     Define class GenPro with attribute(s) and method(s).
     Generate project by template and parameters.
"""

import sys
from inspect import stack

try:
    from pathlib import Path
    from gen_autoconf.pro.read_template import ReadTemplate
    from gen_autoconf.pro.write_template import WriteTemplate
    from ats_utilities.config.cfg.cfg2object import Cfg2Object
    from ats_utilities.console_io.success import success_message
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


class GenPro(object):
    """
        Define class GenPro with attribute(s) and method(s).
        Generate project by template and parameters.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __PRO_STRUCTURE - Project structure
                | __config - Configuration dictionary
                | __current_dir - Current directory
                | __reader - Reader API
                | __writer - Writer API
            :methods:
                | __init__ - Initial constructor
                | get_reader - Getter for reader object
                | get_writer - Getter for writer object
                | gen_project - Generate python tool
    """

    __slots__ = (
        'VERBOSE',
        '__PRO_SUB_STRUCTURE',
        '__config',
        '__current_dir',
        '__reader',
        '__writer'
    )
    VERBOSE = 'GEN_AUTOCONF::PRO::GEN_PRO'
    __PRO_STRUCTURE = '../conf/gen_autoconf_util.cfg'

    def __init__(self, project_name, verbose=False):
        """
            Initial constructor.

            :param project_name: Parameter tool name
            :type project_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        func = stack()[0][3]
        pro_name_txt = 'Argument: expected project_name <str> object'
        pro_name_msg = "{0} {1} {2}".format('def', func, pro_name_txt)
        if project_name is None or not project_name:
            raise ATSBadCallError(pro_name_msg)
        if not isinstance(project_name, str):
            raise ATSTypeError(pro_name_msg)
        verbose_message(GenPro.VERBOSE, verbose, 'Initial generator')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(project_name, verbose=verbose)
        self.__current_dir = Path(__file__).parent
        self.__config = None
        pro_structure = Cfg2Object(
            "{0}/{1}".format(self.__current_dir, GenPro.__PRO_STRUCTURE),
            verbose=verbose
        )
        if pro_structure:
            self.__config = pro_structure.read_configuration(verbose=verbose)

    def get_reader(self):
        """
            Getter for reader object.

            :return: Read template object
            :rtype: <ReadTemplate>
            :exceptions: None
        """
        return self.__reader

    def get_writer(self):
        """
            Getter for writer object.

            :return: Write template object
            :rtype: <WriteTemplate>
            :exceptions: None
        """
        return self.__writer

    def gen_project(self, verbose=False):
        """
            Generate project structure.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Boolean status True (success) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        status = False
        statuses, expected_num_files = [], len(self.__config.keys())
        if bool(self.__config):
            for template_file in self.__config.itervalues():
                template = self.__reader.read(
                    template_file, verbose=verbose
                )
                if template:
                    status_write = self.__writer.write(
                        template, template_file, verbose=verbose
                    )
                    if status_write:
                        statuses.append(status_write)
                    else:
                        break
                else:
                    break
            if all([len(statuses) == expected_num_files, all(statuses)]):
                success_message(
                    GenPro.VERBOSE, 'Successfully loaded templates'
                )
                success_message(
                    GenPro.VERBOSE, 'Successfully written modules'
                )
                status = True
        return True if status else False
