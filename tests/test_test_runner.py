import pytest
import os
from dojo_toolkit.test_runner import BaseTestRunner, SubprocessTestRunner, DoctestTestRunner

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def wrong_cmd():
    return "parangaricutirimicuaro"


@pytest.fixture
def echo_cmd():
    return "echo birl"


@pytest.fixture
def code_path():
    return "/path/to/my/code"


@pytest.fixture
def subprocess_test_runner(code_path):
    return SubprocessTestRunner(code_path)


@pytest.fixture
def base_test_runner(code_path):
    return BaseTestRunner(code_path)


@pytest.fixture
def doctest_test_runner():
    return DoctestTestRunner(os.path.join(MODULE_DIR, "data", "doctest_ok_tests"))


@pytest.fixture
def doctest_test_runner_fail():
    return DoctestTestRunner(os.path.join(MODULE_DIR, "data", "doctest_fail_tests"))


def test_base(base_test_runner, code_path):
    """
    test BaseTestRunner
    """
    assert base_test_runner.code_path == code_path


def test_subprocess(subprocess_test_runner, code_path, echo_cmd):
    """
    test SubprocessTestRunner when cmd not fail
    """
    assert subprocess_test_runner.code_path == code_path
    subprocess_test_runner.cmd = echo_cmd
    assert subprocess_test_runner.cmd == echo_cmd
    assert subprocess_test_runner.run()


def test_subprocess_fail(subprocess_test_runner, code_path, wrong_cmd):
    """
    test SubprocessTestRunner when cmd fail
    """
    assert subprocess_test_runner.code_path == code_path
    subprocess_test_runner.cmd = wrong_cmd
    assert subprocess_test_runner.cmd == wrong_cmd
    assert not subprocess_test_runner.run()


def test_subprocess_doctest_run(doctest_test_runner):
    """
    test a good doctest
    """
    assert doctest_test_runner.run()


def test_subprocess_doctest_run_fail(doctest_test_runner_fail):
    """
    test a fail doctest
    """
    assert not doctest_test_runner_fail.run()
