# -*- coding: UTF-8 -*-

'''
Module
    test_infrastructure.py
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
    Unit tests for infrastructure adapters.
'''

import tempfile
import unittest
from os.path import join
from unittest.mock import MagicMock
from typing import Any, override
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.engine import Checker
from ats_utilities.reporter.engine import Reporter
from ats_utilities.option.command_option import CommandOption
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.generator.igenerator import IGenerator
from gen_autoconf.domain.ports.iservice import IService
from gen_autoconf.infrastructure.icli import ICLI
from gen_autoconf.infrastructure.icli_command import ICLICommand
from gen_autoconf.infrastructure.cli_bundle import CLIBundle
from gen_autoconf.infrastructure.cli import CLI
from gen_autoconf.infrastructure.gen_autoconf_command import GenAutoconfCommand
from gen_autoconf.infrastructure.subprocessor import SubProcessor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_autoconf'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_autoconf/blob/dev/LICENSE'
__version__ = '2.7.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class DummyCommand(ICLICommand):
    '''
        Dummy CLI command for testing CLI / CLIBundle.
    '''

    @property
    @override
    def name(self) -> str:
        return "dummy"

    @property
    @override
    def help_text(self) -> str:
        return "Dummy command for tests"

    @property
    @override
    def options(self) -> list[CommandOption]:
        return [
            CommandOption(name="--foo", help_text="foo parameter", default="bar"),
            CommandOption(name="--req", help_text="required parameter", required=True)
        ]

    @override
    def execute(self, params: dict[str, Any], service: IService) -> dict[str, Any]:
        return {"returncode": 0, "stdout": "dummy executed"}

    @override
    def __str__(self) -> str:
        return f"DummyCommand(name='{self.name}', help_text='{self.help_text}')"


class DummyCLI(ICLI):
    '''
        Dummy CLI implementing ICLI for coverage.
    '''

    @override
    def run(self) -> dict[str, Any]:
        return super().run()

    @override
    def is_initialized(self) -> bool:
        return super().is_initialized()

    @override
    def __str__(self) -> str:
        return super().__str__()


class DummyICLICommand(ICLICommand):
    '''
        Dummy ICLICommand implementing ICLICommand for coverage.
    '''

    @property
    @override
    def name(self) -> str:
        return super().name

    @property
    @override
    def help_text(self) -> str:
        return super().help_text

    @property
    @override
    def options(self) -> list[CommandOption]:
        return super().options

    @override
    def execute(self, params: dict[str, Any], service: IService) -> dict[str, Any]:
        return super().execute(params, service)

    @override
    def __str__(self) -> str:
        return super().__str__()


class TestInfrastructure(unittest.TestCase):
    '''
        Defines infrastructure adapters unit tests.
    '''

    def test_cli_bundle_validation(self) -> None:
        '''
            Tests validation checks of CLIBundle.
        '''
        bundle: CLIBundle = CLIBundle(service=None, parser=None, commands=None)
        with self.assertRaises(ATSValueError) as ctx:
            bundle.validate()
        self.assertEqual(str(ctx.exception), 'service must be provided.')

        bundle_partial1: CLIBundle = CLIBundle(service=MagicMock(spec=IService), parser=None, commands=None)
        with self.assertRaises(ATSValueError) as ctx:
            bundle_partial1.validate()
        self.assertEqual(str(ctx.exception), 'parser must be provided.')

        bundle_partial2: CLIBundle = CLIBundle(
            service=MagicMock(spec=IService), parser=MagicMock(spec=IOptionManager), commands=None
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle_partial2.validate()
        self.assertEqual(str(ctx.exception), 'list of commands must be provided.')

        # Valid bundle validation should not raise error
        bundle_valid: CLIBundle = CLIBundle(
            service=MagicMock(spec=IService),
            parser=MagicMock(spec=IOptionManager),
            commands=[DummyCommand()]
        )
        bundle_valid.validate()

    def test_cli_bundle_helpers(self) -> None:
        '''
            Tests CLIBundle helper methods (merge, to_dict).
        '''
        mock_service: MagicMock = MagicMock(spec=IService)
        mock_parser: MagicMock = MagicMock(spec=IOptionManager)
        cmd: DummyCommand = DummyCommand()

        bundle1: CLIBundle = CLIBundle(service=mock_service, parser=None, commands=None)
        bundle2: CLIBundle = CLIBundle(service=None, parser=mock_parser, commands=[cmd])
        bundle1.merge(bundle2)

        self.assertEqual(bundle1.service, mock_service)
        self.assertEqual(bundle1.parser, mock_parser)
        self.assertEqual(bundle1.commands, [cmd])

        d: dict[str, Any] = bundle1.to_dict()
        self.assertEqual(d["service"], mock_service)
        self.assertEqual(d["parser"], mock_parser)
        self.assertEqual(d["commands"], [cmd])

    def test_cli_init_missing_bundle(self) -> None:
        '''
            Tests CLI initialization raises ValueError when bundle is None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            CLI(None)
        self.assertEqual(str(ctx.exception), 'component bundle (CLIBundle) must be provided.')

    def test_cli_run_executes_command(self) -> None:
        '''
            Tests that CLI.run parses arguments and delegates execution to the matched command.
        '''
        mock_service: MagicMock = MagicMock(spec=IService)
        mock_parser: MagicMock = MagicMock(spec=IOptionManager)
        mock_command: DummyCommand = DummyCommand()

        mock_parser.parse_command.return_value = ("dummy", {"req": "val", "foo": "baz"})

        cli_bundle: CLIBundle = CLIBundle(service=mock_service, parser=mock_parser, commands=[mock_command])
        cli: CLI = CLI(cli_bundle)
        
        self.assertTrue(cli.is_initialized())
        
        res: dict[str, Any] = cli.run()

        mock_parser.parse_command.assert_called_once()
        self.assertEqual(res, {"returncode": 0, "stdout": "dummy executed"})

        self.assertIsNotNone(str(cli))
        self.assertIsNotNone(repr(cli))

    def test_cli_run_unknown_command(self) -> None:
        '''
            Tests CLI behavior when parser returns an unknown command.
        '''
        mock_service: MagicMock = MagicMock(spec=IService)
        mock_parser: MagicMock = MagicMock(spec=IOptionManager)

        mock_parser.parse_command.return_value = ("unknown", {})

        cli_bundle: CLIBundle = CLIBundle(service=mock_service, parser=mock_parser, commands=[])
        cli: CLI = CLI(cli_bundle)
        res: dict[str, Any] = cli.run()

        self.assertEqual(res.get("return_code"), -1)
        self.assertEqual(res.get("stderr"), ["Unknown command"])

    def test_gen_picom_command_metadata_and_execution(self) -> None:
        '''
            Tests GenAutoconfCommand properties and execution.
        '''
        cmd: GenAutoconfCommand = GenAutoconfCommand()
        self.assertEqual(cmd.name, "create")
        self.assertEqual(cmd.help_text, "Generate autoconf project files")
        self.assertEqual(len(cmd.options), 2)
        
        self.assertEqual(cmd.options[0].name, "--name")
        self.assertEqual(cmd.options[1].name, "--output")

        self.assertIsNotNone(str(cmd))
        self.assertIsNotNone(repr(cmd))

        mock_service: MagicMock = MagicMock(spec=IService)
        params: dict[str, str] = {"name": "testproject", "output": "./demo"}
        
        expected_res: dict = {"returncode": 0, "stdout": "project generated"}
        mock_service.execute.return_value = expected_res
        
        res = cmd.execute(params, mock_service)
        mock_service.execute.assert_called_once_with(params=params)
        self.assertEqual(res, expected_res)

    def test_subprocessor_init_failure(self) -> None:
        '''
            Tests SubProcessor init raises ATSValueError when generator is None.
        '''
        with self.assertRaises(ATSValueError) as ctx:
            SubProcessor(None)
        self.assertEqual(str(ctx.exception), 'generator must be provided.')

    def test_subprocessor_run_success(self) -> None:
        '''
            Tests successful execution of SubProcessor run with walks.
        '''
        mock_generator: MagicMock = MagicMock(spec=IGenerator)
        mock_context: ContextBundle = ContextBundle(checker=Checker(), reporter=Reporter(), verbose=False)
        mock_generator.get_shared_context.return_value = mock_context

        with tempfile.TemporaryDirectory() as tmpdir:
            # create nested files
            with open(join(tmpdir, "file1.txt"), "w") as f:
                f.write("content1")
            import os
            os.makedirs(join(tmpdir, "nested"), exist_ok=True)
            with open(join(tmpdir, "nested", "file2.txt"), "w") as f:
                f.write("content2")
            
            mock_generator.generate.return_value = True
            
            sub: SubProcessor = SubProcessor(mock_generator)
            self.assertTrue(sub.is_initialized())
            
            params: dict[str, str] = {"name": "testproject", "output": tmpdir}
            res: dict[str, Any] = sub.run(params)

            self.assertEqual(res["returncode"], 0)
            self.assertIn("testproject successfully generated.", res["stdout"])
            self.assertEqual(res["stderr"], "")

    def test_subprocessor_run_failure(self) -> None:
        '''
            Tests failed execution of SubProcessor run.
        '''
        mock_generator: MagicMock = MagicMock(spec=IGenerator)
        mock_context: ContextBundle = ContextBundle(checker=Checker(), reporter=Reporter(), verbose=False)
        mock_generator.get_shared_context.return_value = mock_context

        mock_generator.generate.return_value = False
        
        sub: SubProcessor = SubProcessor(mock_generator)
        params: dict[str, str] = {"name": "testproject", "output": "./demo"}
        res: dict[str, Any] = sub.run(params)

        self.assertEqual(res["returncode"], 1)
        self.assertEqual(res["stdout"], "")
        self.assertIn("failed to generate testproject project.", res["stderr"])

    def test_subprocessor_is_initialized(self) -> None:
        '''
            Tests is_initialized status of SubProcessor.
        '''
        mock_generator: MagicMock = MagicMock(spec=IGenerator)
        mock_context: ContextBundle = ContextBundle(checker=Checker(), reporter=Reporter(), verbose=False)
        mock_generator.get_shared_context.return_value = mock_context

        sub: SubProcessor = SubProcessor(mock_generator)
        
        mock_generator.is_initialized.return_value = True
        self.assertTrue(sub.is_initialized())

        mock_generator.is_initialized.return_value = False
        self.assertFalse(sub.is_initialized())

        self.assertIsNotNone(str(sub))
        self.assertIsNotNone(repr(sub))

    def test_icli_interface(self) -> None:
        '''
            Tests abstract ICLI interface default implementations.
        '''
        dummy: DummyCLI = DummyCLI()
        self.assertIsNone(dummy.run())
        self.assertIsNone(dummy.is_initialized())
        self.assertIsNone(dummy.__str__())

    def test_iclicommand_interface(self) -> None:
        '''
            Tests abstract ICLICommand interface default implementations.
        '''
        dummy: DummyICLICommand = DummyICLICommand()
        self.assertIsNone(dummy.name)
        self.assertIsNone(dummy.help_text)
        self.assertIsNone(dummy.options)
        self.assertIsNone(dummy.execute({}, None))
        self.assertIsNone(dummy.__str__())
