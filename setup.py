#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
 Module
     setup.py
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
     Define setup for gen_autoconf tool package.
'''

from sys import argv, version_info, prefix, exit
from os.path import abspath, dirname, join, exists
from site import getusersitepackages
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

def install_directory():
    '''
        Return the installation directory, or None.

        :return: Path (success) | None.
        :rtype: <str> | <NoneType>
        :exceptions: None
    '''
    py_version = '{0}.{1}'.format(version_info[0], version_info[1])
    if '--github' in argv:
        index = argv.index('--github')
        argv.pop(index)
        paths = (
            '{0}/lib/python{1}/dist-packages/'.format(prefix, py_version),
            '{0}/lib/python{1}/site-packages/'.format(prefix, py_version)
        )
    else:
        paths = (s for s in (
            '{0}/local/lib/python{1}/dist-packages/'.format(
                prefix, py_version
            ),
            '{0}/local/lib/python{1}/site-packages/'.format(
                prefix, py_version
            )
        ))
    for path in paths:
        print('[setup] check path {0}'.format(path))
        if exists(path):
            print('[setup] using path {0}'.format(path))
            return path
    print('[setup] no installation path found, check {0}\n'.format(prefix))
    return None

INSTALL_DIR = install_directory()

if not INSTALL_DIR:
    print('[setup] force exit from install process')
    exit(127)

THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()

PROGRAMMING_LANG = 'Programming Language :: Python ::'
VERSIONS = ['2.7', '3', '3.2', '3.3', '3.4']
SUPPORTED_PY_VERSIONS = [
    '{0} {1}'.format(PROGRAMMING_LANG, VERSION) for VERSION in VERSIONS
]

LICENSE_PREFIX = 'License :: OSI Approved ::'
LICENSES = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES = [
    '{0}{1}'.format(LICENSE_PREFIX, LICENSE) for LICENSE in LICENSES
]

PYP_CLASSIFIERS = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES

setup(
    name='gen_autoconf',
    version='1.4.1',
    description='Generating C project',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_autoconf/',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='Unix, Linux, Development, ANSI C, autoconf',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=[
        'gen_autoconf',
        'gen_autoconf.pro',
    ],
    install_requires=['ats-utilities'],
    data_files=[
        ('/usr/local/bin/', ['gen_autoconf/run/gen_autoconf_run.py']),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_autoconf/conf/'),
            ['gen_autoconf/conf/gen_autoconf.cfg']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_autoconf/conf/'),
            ['gen_autoconf/conf/gen_autoconf_util.cfg']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_autoconf/conf/'),
            ['gen_autoconf/conf/project.yaml']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_autoconf/conf/template/'),
            ['gen_autoconf/conf/template/README.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_autoconf/conf/template/'),
            ['gen_autoconf/conf/template/Makefile.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_autoconf/conf/template/'),
            ['gen_autoconf/conf/template/configure.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_autoconf/conf/template/src/'),
            ['gen_autoconf/conf/template/src/Makefile.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_autoconf/conf/template/src/'),
            ['gen_autoconf/conf/template/src/main.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'gen_autoconf/conf/log/'),
            ['gen_autoconf/log/gen_autoconf.log']
        )
    ]
)
