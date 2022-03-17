# -*- coding: UTF-8 -*-

'''
 Module
     test_template_dir.py
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
     Defined class TemplateDirTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of TemplateDir.
 Execute
     python3 -m unittest -v test_template_dir
'''

import sys
import unittest
from os.path import dirname, realpath

try:
    from gen_autoconf.pro.config.template_dir import TemplateDir
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/gen_autoconf'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_autoconf/blob/dev/LICENSE'
__version__ = '2.2.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TemplateDirTestCase(unittest.TestCase):
    '''
        Defined class TemplateDirTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of TemplateDir.
        It defines:

            :attributes:
                | template - Template dir object.
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_is_template_dir_ok - test template dir check.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.template = TemplateDir()

    def tearDown(self):
        '''Call after test case.'''
        self.template = None

    def test_is_template_dir_ok(self):
        '''Test template dir check.'''
        self.template.template_dir = '{0}/{1}'.format(
            dirname(realpath(__file__)), '../gen_autoconf/conf/template/'
        )
        self.assertEqual(self.template.is_template_dir_ok(), True)


if __name__ == '__main__':
    unittest.main()
