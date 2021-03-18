import os
from unittest import mock

import pytest

from dojo_toolkit.test_runner import DoctestTestRunner

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def code_file(tmpdir):
    code_file = tmpdir.join('foo.py')
    return code_file


@mock.patch('dojo_toolkit.test_runner.notifier')
def test_doctest_test_runner_real_file_cmd_success(notifier, code_file):
    sound_player_mock = mock.Mock()
    code = [
        '"""',
        '>>> 1 + 2',
        '3',
        '"""',
    ]
    code_file.write('\n'.join(code))
    test_runner = DoctestTestRunner(code_path=str(code_file.dirpath()), sound_player=sound_player_mock)

    assert test_runner.run() is True
    notifier.success.assert_called_once_with('OK TO TALK')


@mock.patch('dojo_toolkit.test_runner.notifier')
def test_doctest_test_runner_real_file_cmd_fail(notifier, code_file):
    sound_player_mock = mock.Mock()
    code = [
        '"""',
        '>>> 1 + 2',
        '4',
        '"""',
    ]
    code_file.write('\n'.join(code))
    test_runner = DoctestTestRunner(code_path=str(code_file.dirpath()), sound_player=sound_player_mock)

    assert test_runner.run() is False
    notifier.fail.assert_called_once_with('NOT OK TO TALK')


def test_doctest_test_runner_run_doctest_success(code_file):
    code = [
        '"""',
        '>>> 1 + 2',
        '3',
        '"""',
    ]
    code_file.write('\n'.join(code))
    test_runner = DoctestTestRunner(code_path=str(code_file.dirpath()), sound_player=None)

    result = test_runner._run_doctest()

    assert result == {'is_success': True, 'output': ''}


def test_doctest_test_runner_run_doctest_fail(code_file):
    code = [
        '"""',
        '>>> 1 + 2',
        '4',
        '"""',
    ]
    code_file.write('\n'.join(code))
    test_runner = DoctestTestRunner(code_path=str(code_file.dirpath()), sound_player=None)

    result = test_runner._run_doctest()

    assert result['is_success'] is False
    output_lines = result['output'].split('\n')
    assert output_lines[2:8] == [
        "Failed example:",
        "    1 + 2",
        "Expected:",
        "    4",
        "Got:",
        "    3",
    ]
