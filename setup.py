#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
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
     Define setup for gen_autoconf package.
"""

from os.path import abspath, dirname, join
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='gen_autoconf',
    version='1.2.0',
    description='Generating C project',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_autoconf/',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='Unix, Linux, Development, ANSI C, autoconf',
    platforms='POSIX',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'
    ],
    packages=[
        'gen_autoconf',
        'gen_autoconf.pro',
    ],
    install_requires=['ats-utilities'],
    data_files=[
        ('/usr/local/bin/', ['gen_autoconf/run/gen_autoconf_run.py']),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/',
            ['gen_autoconf/conf/gen_autoconf.cfg']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/',
            ['gen_autoconf/conf/gen_autoconf_util.cfg']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/template/',
            ['gen_autoconf/conf/template/README.md']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/template/',
            ['gen_autoconf/conf/template/Makefile.am']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/template/',
            ['gen_autoconf/conf/template/configure.ac']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/template/src/',
            ['gen_autoconf/conf/template/src/Makefile.am']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_autoconf/conf/template/src/',
            ['gen_autoconf/conf/template/src/main.c']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_autoconf/log/',
            ['gen_autoconf/log/gen_autoconf.log']
        )
    ]
)
