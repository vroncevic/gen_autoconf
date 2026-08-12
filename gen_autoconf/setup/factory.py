# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the gen_autoconf bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_autoconf.setup.bundle import GenAutoconfBundle
from gen_autoconf.setup.options import GenAutoconfBundleOptions
from gen_autoconf.setup.registry import GenAutoconfBundleRegistry
from gen_autoconf.setup.dependencies import GenAutoconfBundleDependencies
from gen_autoconf.setup.opt_validator import GenAutoconfBundleOptionsValidator
from gen_autoconf.setup.keys import GenAutoconfBundleKeys
from gen_autoconf.core.service.engine import Service
from gen_autoconf.infrastructure.subprocessor import SubProcessor
from gen_autoconf.infrastructure.cli.engine import CLI
from gen_autoconf.infrastructure.cli.setup.bundle import CLIBundle
from gen_autoconf.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_autoconf.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_autoconf.infrastructure.command.command import CommandBundle
from gen_autoconf.infrastructure.command.gen_autoconf_command_definition import GenAutoconfCommandDefinition
from gen_autoconf.infrastructure.command.gen_autoconf_command_executor import GenAutoconfCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_autoconf'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_autoconf/blob/dev/LICENSE'
__version__ = '2.7.9'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenAutoconfBundleFactory:
    '''
        Factory for creating the gen_autoconf bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_autoconf info file.
            :methods:
                | create_bundle - Creates the gen_autoconf bundle with optional pre-configured options.
    '''

    _info_file: str = 'gen_autoconf/infrastructure/config/gen_autoconf.cfg'

    @classmethod
    def create_bundle(cls, options: GenAutoconfBundleOptions | None = None) -> GenAutoconfBundle:
        '''
            Creates the gen_autoconf bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_autoconf bundle.
            :return: The gen_autoconf bundle.
            :exceptions:
                | ATSValueError: The gen_autoconf bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_autoconf bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_autoconf bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_autoconf bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_autoconf bundle must be provided and have proper values.
                | ATSTypeError:  The gen_autoconf bundle must be an instance of GenAutoconfBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenAutoconfBundleOptionsValidator.validate(options)

        info_file = options.get(GenAutoconfBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_autoconf_definition: GenAutoconfCommandDefinition = GenAutoconfCommandDefinition()

        gen_autoconf_bundle: CommandBundle = CommandBundle(
            definition=gen_autoconf_definition,
            executor=GenAutoconfCommandExecutor(gen_autoconf_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_autoconf_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenAutoconfBundleRegistry.create_bundle(
            dependencies=GenAutoconfBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )
