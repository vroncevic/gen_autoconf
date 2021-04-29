# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Defined class GenPro with attribute(s) and method(s).
     Generate project by template and parameters.
'''

import sys

try:
    from pathlib import Path
    from gen_autoconf.pro.read_template import ReadTemplate
    from gen_autoconf.pro.write_template import WriteTemplate
    from ats_utilities.checker import ATSChecker
    from ats_utilities.cooperative import CooperativeMeta
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.success import success_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, https://vroncevic.github.io/gen_autoconf'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_autoconf/blob/dev/LICENSE'
__version__ = '2.0.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenPro(FileChecking):
    '''
        Defined class GenPro with attribute(s) and method(s).
        Generate project by template and parameters.
        It defines:

            :attributes:
                | __metaclass__ - setting cooperative metaclasses.
                | GEN_VERBOSE - console text indicator for process-phase.
                | PRO_STRUCTURE - project structure.
                | __config - configuration dictionary.
                | __reader - reader API.
                | __writer - writer API.
            :methods:
                | __init__ - initial constructor.
                | get_reader - getter for reader object.
                | get_writer - getter for writer object.
                | gen_project - generate python tool.
                | __str__ - dunder method for GenPro.
    '''

    __metaclass__ = CooperativeMeta
    GEN_VERBOSE = 'GEN_AUTOCONF::PRO::GEN_PRO'
    PRO_STRUCTURE = '../conf/project.yaml'

    def __init__(self, project_name, verbose=False):
        '''
            Initial constructor.

            :param project_name: parameter tool name.
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
        verbose_message(GenPro.GEN_VERBOSE, verbose, 'init generator')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(project_name, verbose=verbose)
        project = '{0}/{1}'.format(
            Path(__file__).parent, GenPro.PRO_STRUCTURE
        )
        self.check_path(file_path=project, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=project, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(project)
            self.__config = yml2obj.read_configuration()
        else:
            self.__config = None

    def get_reader(self):
        '''
            Getter for reader object.

            :return: read template object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for writer object.

            :return: write template object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def gen_project(self, verbose=False):
        '''
            Generate project structure.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status, statuses = False, []
        templates = self.__config['templates'].split(' ')
        modules = self.__config['modules'].split(' ')
        expected_num_files = len(templates)
        if bool(self.__config) and expected_num_files == len(modules):
            for template_file, module_file in zip(templates, modules):
                template = self.__reader.read(
                    template_file, verbose=verbose
                )
                if template:
                    status_write = self.__writer.write(
                        template, module_file, verbose=verbose
                    )
                    if status_write:
                        statuses.append(status_write)
                    else:
                        break
                else:
                    break
            if all([len(statuses) == expected_num_files, all(statuses)]):
                success_message(
                    GenPro.GEN_VERBOSE, 'successfully loaded templates'
                )
                success_message(
                    GenPro.GEN_VERBOSE, 'successfully written modules'
                )
                status = True
        return status

    def __str__(self):
        '''
            Dunder method for GenPro.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__reader), str(self.__writer), str(self.__config)
        )
