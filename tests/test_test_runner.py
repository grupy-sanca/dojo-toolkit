import os
from unittest import mock

import pytest

from dojo_toolkit.test_runner import DoctestTestRunner, PytestTestRunner, get_test_runner

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def code_file(tmpdir):
    code_file = tmpdir.join("foo.py")
    return code_file


def write_docstring(f, code):
    code = docstringfy(code)
    f.write(code)


@mock.patch("dojo_toolkit.test_runner.notifier")
def test_doctest_test_runner_real_file_cmd_success(notifier, code_file):
    sound_player_mock = mock.Mock()
    code = """
        >>> 1 + 2
        3
    """
    write_docstring(code_file, code)
    test_runner = DoctestTestRunner(
        code_path=str(code_file.dirpath()), sound_player=sound_player_mock
    )

    assert test_runner.run() is True
    notifier.success.assert_called_once_with("OK TO TALK")


@mock.patch("builtins.print")
@mock.patch("dojo_toolkit.test_runner.notifier")
def test_doctest_test_runner_real_file_cmd_fail(notifier_mock, print_mock, code_file):
    sound_player_mock = mock.Mock()
    code = """
        >>> 1 + 2
        4
    """
    write_docstring(code_file, code)
    test_runner = DoctestTestRunner(
        code_path=str(code_file.dirpath()), sound_player=sound_player_mock
    )

    assert test_runner.run() is False
    notifier_mock.fail.assert_called_once_with("NOT OK TO TALK")
    assert print_mock.call_count == 2


def test_doctest_test_runner_run_doctest_success(code_file):
    code = """
        >>> 1 + 2
        3
    """
    write_docstring(code_file, code)
    test_runner = DoctestTestRunner(code_path=str(code_file.dirpath()), sound_player=None)

    result = test_runner._run_test()

    assert result == {"is_success": True, "output": ""}


def test_doctest_test_runner_run_doctest_fail(code_file):
    code = """
        >>> 1 + 2
        4
    """
    write_docstring(code_file, code)
    test_runner = DoctestTestRunner(code_path=str(code_file.dirpath()), sound_player=None)

    result = test_runner._run_test()

    assert result["is_success"] is False
    output_lines = result["output"].split("\n")
    assert output_lines[2:8] == [
        "Failed example:",
        "    1 + 2",
        "Expected:",
        "    4",
        "Got:",
        "    3",
    ]


def docstringfy(code):
    result = '"""\n'
    lines = code.split("\n")
    for line in lines[1:-1]:
        result += line.strip() + "\n"
    result += '"""'
    return result


def test_docstringfy():
    code = """
    >>> 1 + 2
    3
    """

    assert docstringfy(code) == '"""\n>>> 1 + 2\n3\n"""'


@pytest.mark.parametrize(
    "runner,test_runner", [("doctest", DoctestTestRunner), ("pytest", PytestTestRunner)]
)
def test_get_test_runner(runner, test_runner, code_file):
    test_runner_got = get_test_runner(
        None, runner, code_path=str(code_file.dirpath()), sound_player=None
    )

    assert isinstance(test_runner_got, test_runner)


def test_get_test_runner_invalid_runner(code_file):
    with pytest.raises(NotImplementedError):
        get_test_runner(None, "", code_path=str(code_file.dirpath()), sound_player=None)
