"""
Module for running tests like doctest and unittest
"""
from abc import ABC, abstractmethod
import os
from subprocess import PIPE, Popen, call

from .notifier import notifier


class SubprocessTestRunner(ABC):
    """
    Base class to all test runners that use subprocess module.
    """
    cmd = None

    def __init__(self, code_path, sound_player):
        self.code_path = code_path
        self.sound_player = sound_player

    def run(self):
        """
        run a test cmd using subprocess
        """
        process = Popen(
            [self.cmd, self.code_path],
            shell=True,
            stdout=PIPE,
            universal_newlines=True,
        )
        process.wait()

        success = process.returncode == 0
        self.handle_result(success)
        if os.name == "nt":
            command = "cls"
        else:
            command = "clear"
        tmp = call(command, shell=True)  # noqa
        self.handle_terminal_output('\n'.join(str(line) for line in process.stdout.readlines()))

        return success

    def handle_result(self, success):
        if success:
            self.handle_success()
        else:
            self.handle_failure()

    def handle_success(self):
        print('\nTests passed!\n')
        notifier.success('OK TO TALK')
        self.sound_player.play_success()

    def handle_failure(self):
        print('\nTests failed!\n')
        notifier.fail('NOT OK TO TALK')

    @abstractmethod
    def handle_terminal_output(self, output_string):
        pass


class DoctestTestRunner(SubprocessTestRunner):
    """
    Subprocess doctest runner
    """
    cmd = "python -m doctest"
