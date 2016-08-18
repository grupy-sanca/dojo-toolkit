import time

from watchdog.events import PatternMatchingEventHandler


class DojoCodeHandler(PatternMatchingEventHandler):
    """Handles the python file changes"""
    patterns = ['*.py']
    ignore_directories = True

    def __init__(self, *args, **kwargs):
        self.notifier = kwargs.pop('notifier')
        self.test_runner = kwargs.pop('test_runner')

        super(DojoCodeHandler, self).__init__(*args, **kwargs)

        self.last_time = time.time()

    def on_modified(self, event):
        """Called when a file in the dojo directory is modified
        runs the doctest and display a notification
        Green for 'ok to talk, test passing'
        Red for 'not ok to talk, test failing'
        """

        new_time = time.time()
        diff = new_time - self.last_time
        if diff > 2:
            self.last_time = new_time
        else:
            return

        if self.test_runner.run():
            self.notifier.success('OK TO TALK')
            print('Tests passing!')
        else:
            self.notifier.fail('NOT OK TO TALK')
