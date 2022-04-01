# -*- coding: UTF-8 -*-

'''
 Module
     test_write_template.py
 Copyright
     Copyright (C) 2022 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class WriteTemplateTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of WriteTemplate.
 Execute
     python3 -m unittest -v test_write_template
'''

import sys
import unittest
from os.path import dirname, realpath

try:
    from gen_autoconf.pro.write_template import WriteTemplate
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/gen_autoconf'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_autoconf/blob/dev/LICENSE'
__version__ = '2.3.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplateTestCase(unittest.TestCase):
    '''
        Defined class WriteTemplateTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of WriteTemplate.
        It defines:

            :attributes:
                | template - Write template object.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_write_template - test write template check.
    '''

    templates = [{'autogen.sh': '#!/bin/sh\n#\n# autogen.sh\n# Copyright (C) 2021 ${PRO} Vladimir Roncevic <elektron.ronca@gmail.com>\n#\n# ${PRO} is free software: you can redistribute it and/or modify it\n# under the terms of the GNU General Public License as published by the\n# Free Software Foundation, either version 3 of the License, or\n# (at your option) any later version.\n#\n# ${PRO} is distributed in the hope that it will be useful, but\n# WITHOUT ANY WARRANTY; without even the implied warranty of\n# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n# See the GNU General Public License for more details.\n#\n# You should have received a copy of the GNU General Public License along\n# with this program. If not, see <http://www.gnu.org/licenses/>.\n#\n\nautoreconf --install\n'}, {'configure.ac': 'dnl\ndnl configure.ac\ndnl Copyright (C) 2021 ${PRO} Vladimir Roncevic <elektron.ronca@gmail.com>\ndnl\ndnl ${PRO} is free software: you can redistribute it and/or modify it\ndnl under the terms of the GNU General Public License as published by the\ndnl Free Software Foundation, either version 3 of the License, or\ndnl (at your option) any later version.\ndnl\ndnl ${PRO} is distributed in the hope that it will be useful, but\ndnl WITHOUT ANY WARRANTY; without even the implied warranty of\ndnl MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\ndnl See the GNU General Public License for more details.\ndnl\ndnl You should have received a copy of the GNU General Public License along\ndnl with this program. If not, see <http://www.gnu.org/licenses/>.\ndnl\n\nAC_INIT([automake_${PRO}], [1.0], [bug-automake@gnu.org])\nAM_INIT_AUTOMAKE([-Wall -Werror foreign])\nAC_PROG_CC\nAC_CONFIG_HEADERS([config.h])\nAC_CONFIG_FILES([\n    Makefile\n    src/Makefile\n])\nAC_OUTPUT\n\n'}, {'Makefile.am': '#\n# Makefile.am\n# Copyright (C) 2021 ${PRO} Vladimir Roncevic <elektron.ronca@gmail.com>\n#\n# ${PRO} is free software: you can redistribute it and/or modify it\n# under the terms of the GNU General Public License as published by the\n# Free Software Foundation, either version 3 of the License, or\n# (at your option) any later version.\n#\n# ${PRO} is distributed in the hope that it will be useful, but\n# WITHOUT ANY WARRANTY; without even the implied warranty of\n# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n# See the GNU General Public License for more details.\n#\n# You should have received a copy of the GNU General Public License along\n# with this program. If not, see <http://www.gnu.org/licenses/>.\n#\n\nSUBDIRS = src\ndist_doc_DATA = README.md\n\n'}, {'README.md': '${PRO}\n'}, {'src/main.c': '/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */\n/*\n * main.c\n * Copyright (C) 2021 ${PRO} Vladimir Roncevic <elektron.ronca@gmail.com>\n *\n * ${PRO} is free software: you can redistribute it and/or modify it\n * under the terms of the GNU General Public License as published by the\n * Free Software Foundation, either version 3 of the License, or\n * (at your option) any later version.\n *\n * ${PRO} is distributed in the hope that it will be useful, but\n * WITHOUT ANY WARRANTY; without even the implied warranty of\n * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n * See the GNU General Public License for more details.\n *\n * You should have received a copy of the GNU General Public License along\n * with this program. If not, see <http://www.gnu.org/licenses/>.\n */\n\n#include <stdio.h>\n#include <config.h>\n\nint main(void) {\n    puts("Hello world from " PACKAGE_STRING);\n    return 0;\n}\n\n'}, {'src/Makefile.am': '#\n# Makefile.am\n# Copyright (C) 2021 ${PRO} Vladimir Roncevic <elektron.ronca@gmail.com>\n#\n# ${PRO} is free software: you can redistribute it and/or modify it\n# under the terms of the GNU General Public License as published by the\n# Free Software Foundation, either version 3 of the License, or\n# (at your option) any later version.\n#\n# ${PRO} is distributed in the hope that it will be useful, but\n# WITHOUT ANY WARRANTY; without even the implied warranty of\n# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n# See the GNU General Public License for more details.\n#\n# You should have received a copy of the GNU General Public License along\n# with this program. If not, see <http://www.gnu.org/licenses/>.\n#\n\nbin_PROGRAMS = autotools_${PRO}\nautotools_${PRO}_SOURCES = main.c\n\n'}]

    def setUp(self):
        '''Call before test case.'''
        self.template = WriteTemplate()

    def tearDown(self):
        '''Call after test case.'''
        self.template = None

    def test_write_template(self):
        '''Test write template check.'''
        self.assertEqual(
            self.template.write(
                WriteTemplateTestCase.templates, 'simple_test'
            ),
            True
        )


if __name__ == '__main__':
    unittest.main()
