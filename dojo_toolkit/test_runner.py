from subprocess import Popen


class BaseTestRunner():
    def __init__(self, code_path):
        self.code_path = code_path


class DoctestTestRunner(BaseTestRunner):
    def run(self):
        cmd = "python -m doctest {}/*.py".format(self.code_path)
        process = Popen([cmd], shell=True)
        process.wait()
        return process.returncode == 0
