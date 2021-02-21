"""
Module for running tests like doctest and unittest
"""
import os
from subprocess import PIPE, Popen, call

from .notifier import notifier


class DoctestTestRunner:
    """
    Base class to all test runners that use subprocess module.
    """
    cmd = "python -m doctest"

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

        is_success = process.returncode == 0
        self.handle_result(is_success)
        command = "cls" if os.name == "nt" else "clear"
        tmp = call(command, shell=True)  # noqa
        print('\n'.join(str(line) for line in process.stdout.readlines()))

        return is_success

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
