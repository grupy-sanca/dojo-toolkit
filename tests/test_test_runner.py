import os
from unittest import mock

import pytest

from dojo_toolkit.test_runner import DoctestTestRunner

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def code_path():
    return "/path/to/my/code"


@mock.patch('dojo_toolkit.test_runner.notifier')
def test_doctest_test_runner_real_file_cmd_success(notifier, tmpdir):
    sound_player_mock = mock.Mock()
    code_file = tmpdir.join('foo.py')
    code = [
        '"""',
        '>>> 1 + 2',
        '3',
        '"""',
    ]
    code_file.write('\n'.join(code))
    test_runner = DoctestTestRunner(code_path=str(code_file), sound_player=sound_player_mock)

    assert test_runner.run() is True
    notifier.success.assert_called_once_with('OK TO TALK')
