#!/usr/bin/python
import time
import sys
from pgi.repository import Notify
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class pythonPatternHandler(PatternMatchingEventHandler):
    """Handles the python file changes"""
    patterns = ['*.py']
    ignore_directories = True
    last_time = time.time()
    notification = None

    # TODO: icon, runs doctest with popen and its return
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
        Notify.init('name')
        summ = 'summ'
        body = 'body'
        self.notification = Notify.Notification.new(summ, body, 'red-green-icon')
        self.notification.set_urgency(2)
        self.notification.show()


if __name__ == "__main__":
    event_handler = pythonPatternHandler()
    observer = Observer()
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
