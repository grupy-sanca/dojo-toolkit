import os
from unittest import mock

import pytest

from dojo_toolkit.test_runner import DoctestTestRunner

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def code_path():
    return "/path/to/my/code"


class MockTestRunner(DoctestTestRunner):
    cmd = "echo"


@pytest.fixture
def mock_test_runner(code_path):
    return MockTestRunner(code_path, sound_player=mock.Mock())


class WrongTestRunner(DoctestTestRunner):
    cmd = "parangaricutirimicuaro"


@pytest.fixture
def wrong_test_runner(code_path):
    with mock.patch('dojo_toolkit.test_runner.notifier'):
        return WrongTestRunner(code_path, sound_player=mock.Mock())


@mock.patch('dojo_toolkit.test_runner.notifier')
def test_doctest_test_runner_cmd_success(notifier, mock_test_runner, code_path):
    assert 'echo' in mock_test_runner.cmd
    assert mock_test_runner.run()


@mock.patch('dojo_toolkit.test_runner.notifier')
def test_doctest_test_runner_cmd_fail(notifier, wrong_test_runner, code_path):
    assert 'parangaricutirimicuaro' in wrong_test_runner.cmd
    assert not wrong_test_runner.run()
