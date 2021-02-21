"""
Module for running tests like doctest and unittest
"""
import os
import subprocess

from .notifier import notifier


def clear_screen():
    command = "cls" if os.name == "nt" else "clear"
    subprocess.call(command, shell=True)  # noqa


class DoctestTestRunner:
    """
    Base class to all test runners that use subprocess module.
    """

    def __init__(self, code_path, sound_player):
        self.code_path = code_path
        self.sound_player = sound_player

    def run(self):
        """
        run a test cmd using subprocess
        """

        result = subprocess.run(
            ["python", "-m", "doctest", self.code_path],
            capture_output=True
        )
        is_success = result.returncode == 0

        clear_screen()

        self.handle_result(is_success)
        print('\n'.join(str(line) for line in result.stdout))

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
