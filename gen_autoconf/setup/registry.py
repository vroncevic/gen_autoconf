# -*- coding: UTF-8 -*-

'''
Module
    registry.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Encapsulates core gen_autoconf components for simplification of gen_autoconf bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_autoconf.core.service.iservice import IService
from gen_autoconf.core.service.isubprocessor import ISubProcessor
from gen_autoconf.infrastructure.cli.icli import ICLI
from gen_autoconf.setup.bundle import GenAutoconfBundle
from gen_autoconf.setup.validator import GenAutoconfBundleValidator
from gen_autoconf.setup.keys import GenAutoconfBundleKeys
from gen_autoconf.setup.dependencies import GenAutoconfBundleDependencies
from gen_autoconf.setup.dep_validator import GenAutoconfBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_autoconf'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_autoconf/blob/dev/LICENSE'
__version__ = '2.7.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenAutoconfBundleRegistry:
    '''
        Encapsulates core gen_autoconf components for simplification of gen_autoconf bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_autoconf bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenAutoconfBundleDependencies) -> GenAutoconfBundle:
        '''
            Creates the gen_autoconf bundle.

            :param dependencies: The gen_autoconf bundle dependencies.
            :return: The gen_autoconf bundle.
            :exceptions:
                | ATSValueError: The gen_autoconf bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_autoconf bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_autoconf bundle must be provided and have proper values.
                | ATSTypeError:  The gen_autoconf bundle must be an instance of GenAutoconfBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenAutoconfBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenAutoconfBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenAutoconfBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenAutoconfBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenAutoconfBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenAutoconfBundle = GenAutoconfBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenAutoconfBundleValidator.validate(bundle)

        return bundle
