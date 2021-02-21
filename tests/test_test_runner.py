import os
from unittest import mock

import pytest

from dojo_toolkit.test_runner import DoctestTestRunner

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def code_path():
    return "/path/to/my/code"


@mock.patch('dojo_toolkit.test_runner.notifier')
def test_doctest_test_runner_cmd_success(notifier, code_path):
    class MockTestRunner(DoctestTestRunner):
        cmd = "echo"

    test_runner = MockTestRunner(code_path, sound_player=mock.Mock())

    assert 'echo' in test_runner.cmd
    assert test_runner.run()


@mock.patch('dojo_toolkit.test_runner.notifier')
def test_doctest_test_runner_cmd_fail(notifier, code_path):
    class WrongTestRunner(DoctestTestRunner):
        cmd = "parangaricutirimicuaro"

    with mock.patch('dojo_toolkit.test_runner.notifier'):
        test_runner = WrongTestRunner(code_path, sound_player=mock.Mock())

    assert 'parangaricutirimicuaro' in test_runner.cmd
    assert not test_runner.run()
