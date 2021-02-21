"""
Module for running tests like doctest and unittest
"""
import os
import subprocess

from .notifier import notifier


class DoctestTestRunner:
    def __init__(self, code_path, sound_player):
        self.code_path = code_path
        self.sound_player = sound_player

    def run(self):
        result = self._run_doctest()
        self._clear_screen()
        self._handle_result(result['is_success'])
        print(result['output'])
        return result['is_success']

    def _run_doctest(self):
        result = subprocess.run(
            ["python", "-m", "doctest", self.code_path],
            capture_output=True
        )

        return {
            'is_success': result.returncode == 0,
            'output': result.stdout.decode('utf-8'),
        }

    def _clear_screen(self):
        command = "cls" if os.name == "nt" else "clear"
        subprocess.call(command, shell=True)

    def _handle_result(self, success):
        if success:
            self._handle_success()
        else:
            self._handle_failure()

    def _handle_success(self):
        print('\nTests passed!\n')
        notifier.success('OK TO TALK')
        self.sound_player.play_success()

    def _handle_failure(self):
        print('\nTests failed!\n')
        notifier.fail('NOT OK TO TALK')
