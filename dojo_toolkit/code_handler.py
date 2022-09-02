import time

from watchdog.events import PatternMatchingEventHandler


class DojoCodeHandler(PatternMatchingEventHandler):
    """Handles the python file changes"""

    patterns = ["*.py"]
    ignore_directories = True
    min_test_time_interval = 2

    def __init__(self, *args, **kwargs):
        self.dojo = kwargs.pop("dojo")
        self.test_runner = kwargs.pop("test_runner")

        super(DojoCodeHandler, self).__init__(*args, **kwargs)

        self.last_test_run_time = time.time()

    def get_last_test_run_interval(self):
        return time.time() - self.last_test_run_time

    def on_modified(self, event):
        """Called when a file in the dojo directory is modified
        runs the doctest and display a notification
        Green for 'ok to talk, test passing'
        Red for 'not ok to talk, test failing'
        """

        if not self.dojo.round_started:
            return
        if self.get_last_test_run_interval() < self.min_test_time_interval:
            return
        self.last_test_run_time = time.time()

        self.test_runner.run()
