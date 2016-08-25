"""
Tests of test_runner.py
"""

import os
from dojo_toolkit.test_runner import BaseTestRunner, SubprocessTestRunner, DoctestTestRunner

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


def test_base():
    """
    test BaseTestRunner
    """
    code_path = "/path/to/my/code"
    base_test = BaseTestRunner(code_path)
    assert base_test.code_path == code_path
    base_test.code_path = "another/path"
    assert base_test.code_path != code_path


def test_subprocess():
    """
    test SubprocessTestRunner
    """
    code_path = "/path/to/my/code"
    not_cmd = "parangaricutirimicuaro"
    cmd = "echo hi"

    subprocess_test = SubprocessTestRunner(code_path)
    assert subprocess_test.code_path == code_path

    # tests when cmd fail
    subprocess_test.cmd = not_cmd
    assert subprocess_test.cmd == not_cmd
    assert not subprocess_test.run()

    # test when cmd not fail
    subprocess_test.cmd = cmd
    assert subprocess_test.cmd == cmd
    assert subprocess_test.run()


def test_subproces_doctest():
    """
    test DoctestTestRunner
    """
    doctest_test = DoctestTestRunner(os.path.join(MODULE_DIR, "data", "doctest_ok_tests"))
    doctest_test.run()
    assert doctest_test.run()

    doctest_test.code_path = os.path.join(MODULE_DIR, "data", "doctest_fail_tests")
    doctest_test.run()

    assert doctest_test.code_path == os.path.join(MODULE_DIR, "data", "doctest_fail_tests")
    assert not doctest_test.run()
