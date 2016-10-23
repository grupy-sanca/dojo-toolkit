import os

import pytest

from dojo_toolkit.test_runner import SubprocessTestRunner, DoctestTestRunner
from dojo_toolkit.utils import mock

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def code_path():
    return "/path/to/my/code"


class MockTestRunner(SubprocessTestRunner):
    cmd = "echo '{}'"


@pytest.fixture
def mock_test_runner(code_path):
    return MockTestRunner(code_path, sound_player=mock.Mock())


class WrongTestRunner(DoctestTestRunner):
    cmd = "parangaricutirimicuaro '{}'"


@pytest.fixture
def wrong_test_runner(code_path):
    with mock.patch('dojo_toolkit.test_runner.notifier'):
        return WrongTestRunner(code_path, sound_player=mock.Mock())


@mock.patch('dojo_toolkit.test_runner.notifier')
def test_mock(notifier, mock_test_runner, code_path):
    """
    test SubprocessTestRunner when cmd not fail
    """
    assert code_path in mock_test_runner.cmd
    assert 'echo' in mock_test_runner.cmd
    assert mock_test_runner.run()


@mock.patch('dojo_toolkit.test_runner.notifier')
def test_mock_fail(notifier, wrong_test_runner, code_path):
    """
    test SubprocessTestRunner when cmd fail
    """
    assert code_path in wrong_test_runner.cmd
    assert 'parangaricutirimicuaro' in wrong_test_runner.cmd
    assert not wrong_test_runner.run()
