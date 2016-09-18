"""
Module for running tests like doctest and unittest
"""
from subprocess import Popen


class BaseTestRunner():
    """
    Base class to all test runners
    """

    def __init__(self, code_path):
        self.code_path = code_path


class SubprocessTestRunner(BaseTestRunner):
    """
    Base class to all test runners that use subprocess module.
    """
    cmd = ""

    def run(self):
        """
        run a test cmd using subprocess
        """
        cmd = self.cmd.format(self.code_path)
        process = Popen([cmd], shell=True)
        process.wait()
        return process.returncode == 0


class DoctestTestRunner(SubprocessTestRunner):
    """
    Subprocess doctest runner
    """
    cmd = "python -m doctest {}/*.py"
