"""
Module for running tests like doctest and unittest
"""
import os
import subprocess

from clint.textui import colored

from dojo_toolkit.notifier import notifier


def get_test_runner(test_runner, runner, code_path, sound_player):
    if test_runner:
        return test_runner
    if runner == "doctest":
        return DoctestTestRunner(code_path, sound_player)
    elif runner == "pytest":
        return PytestTestRunner(code_path, sound_player)
    else:
        raise NotImplementedError("Invalid runner")


class LocalTestRunner:
    def __init__(self, code_path, sound_player):
        self.code_path = code_path
        self.sound_player = sound_player

    def _run_test(self):
        raise NotImplementedError("_run_test() must be implemented")

    def run(self):
        result = self._run_test()
        self._clear_screen()
        self._handle_result(result["is_success"])
        print(result["output"])
        return result["is_success"]

    def _clear_screen(self):
        command = "cls" if os.name == "nt" else "clear"
        subprocess.call(command, shell=True)

    def _handle_result(self, success):
        if success:
            self._handle_success()
        else:
            self._handle_failure()

    def _handle_success(self):
        print(getattr(colored, "green")("\nTests passed!\n"))
        notifier.success("OK TO TALK")
        self.sound_player.play_success()

    def _handle_failure(self):
        print(getattr(colored, "red")("\nTests failed!\n"))
        notifier.fail("NOT OK TO TALK")


class DoctestTestRunner(LocalTestRunner):
    def _run_test(self):
        result = subprocess.run(
            ["python -m doctest " + self.code_path + "/*.py"],
            capture_output=True,
            shell=True,
            encoding="utf-8",
        )

        return {
            "is_success": result.returncode == 0,
            "output": result.stdout,
        }


class PytestTestRunner(LocalTestRunner):
    def _run_test(self):
        result = subprocess.run(
            ["python -m pytest " + self.code_path + "/*.py"],
            capture_output=True,
            shell=True,
            encoding="utf-8",
        )

        return {
            "is_success": result.returncode == 0,
            "output": result.stdout,
        }
