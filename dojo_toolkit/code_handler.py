import time

from watchdog.events import PatternMatchingEventHandler


class DojoCodeHandler(PatternMatchingEventHandler):
    """Handles the python file changes"""
    patterns = ['*.py']
    ignore_directories = True
    min_test_time_interval = 2

    def __init__(self, *args, **kwargs):
        self.notifier = kwargs.pop('notifier')
        self.test_runner = kwargs.pop('test_runner')
        self.sound_player = kwargs.pop('sound_player')

        super(DojoCodeHandler, self).__init__(*args, **kwargs)

        self.last_test_run_time = time.time()

    def get_last_test_run_interval(self):
        return time.time() - self.last_test_run_time

    def handle_success(self):
        self.notifier.success('OK TO TALK')
        self.sound_player.play_success()
        print('Tests passed!')

    def handle_fail(self):
        self.notifier.fail('NOT OK TO TALK')

    def on_modified(self, event):
        """Called when a file in the dojo directory is modified
        runs the doctest and display a notification
        Green for 'ok to talk, test passing'
        Red for 'not ok to talk, test failing'
        """

        if self.get_last_test_run_interval() < self.min_test_time_interval:
            return

        self.last_test_run_time = time.time()

        if self.test_runner.run():
            self.handle_success()
        else:
            self.handle_fail()
