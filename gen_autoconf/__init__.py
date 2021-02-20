# -*- coding: UTF-8 -*-

"""
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
     Define class GenAutoconf with attribute(s) and method(s).
     Load a base info, create an CLI interface and run operation(s).
"""

import sys
from os.path import exists

try:
    from pathlib import Path
    from gen_autoconf.pro import GenPro
    from ats_utilities.cli.cfg_cli import CfgCLI
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
except ImportError as error_message:
    MSG = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MSG)  # Force close python ATS ##################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenAutoconf(CfgCLI):
    """
        Define class GenAutoconf with attribute(s) and method(s).
        Load a base info, create an CLI interface and run operation(s).
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __CONFIG - Configuration file path.
                | __OPS - Tool options (list).
            :methods:
                | __init__ - Initial constructor.
                | process - Process and run tool option(s).
    """

    __slots__ = ('VERBOSE', '__CONFIG', '__OPS')
    VERBOSE = 'GEN_AUTOCONF'
    __CONFIG = '/conf/gen_autoconf.cfg'
    __OPS = ['-g', '--gen', '-v']

    def __init__(self, verbose=False):
        """
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(GenAutoconf.VERBOSE, verbose, 'init configuration')
        current_dir = Path(__file__).resolve().parent
        base_info = "{0}{1}".format(current_dir, GenAutoconf.__CONFIG)
        CfgCLI.__init__(self, base_info, verbose=verbose)
        if self.tool_operational:
            self.add_new_option(
                GenAutoconf.__OPS[0], GenAutoconf.__OPS[1],
                dest='gen', help='Generate project'
            )
            self.add_new_option(
                GenAutoconf.__OPS[2], action="store_true", default=False,
                help='activate verbose mode for generation'
            )

    def process(self, verbose=False):
        """
            Process and run operation.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True (success) | False.
            :rtype: <bool>
            :exceptions: None
        """
        status = False
        if self.tool_operational:
            num_of_args_sys = len(sys.argv)
            if num_of_args_sys > 1:
                option = sys.argv[1]
                if option not in GenAutoconf.__OPS:
                    sys.argv = []
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            opts, args = self.parse_args(sys.argv)
            num_of_args, pro_exists = len(args), exists(opts.gen)
            if not pro_exists:
                if num_of_args >= 1 and bool(opts.gen):
                    print(
                        "{0} {1} [{2}]".format(
                            "[{0}]".format(GenAutoconf.VERBOSE.lower()),
                            'generating project', opts.gen
                        )
                    )
                    generator = GenPro(opts.gen, verbose=opts.v or verbose)
                    status = generator.gen_project(verbose=opts.v or verbose)
                    if status:
                        success_message(GenAutoconf.VERBOSE, 'done\n')
                    else:
                        error_message(
                            GenAutoconf.VERBOSE, 'failed to generate project'
                        )
                else:
                    error_message(
                        GenAutoconf.VERBOSE, 'provide project name'
                    )
            else:
                error_message(GenAutoconf.VERBOSE, 'project already exist')
        else:
            error_message(GenAutoconf.VERBOSE, 'tool is not operational')
        return True if status else False
