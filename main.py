#!/usr/bin/python
import time
import sys

from pgi.repository import Notify
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from subprocess import Popen


class PythonPatternHandler(PatternMatchingEventHandler):
    """Handles the python file changes"""
    patterns = ['*.py']
    ignore_directories = True
    last_time = time.time()
    Notify.init('notification')
    notification = Notify.Notification.new('', '', '')

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
        program = event.src_path
        cmd = "python -m doctest " + program
        process = Popen([cmd], shell=True)
        process.wait()
        if process.returncode == 0:
            self.notification.close()
            self.notification.update('OK TO TALK', '', 'g.jpg')
            self.notification.set_timeout(5*60*1000)
            self.notification.show()
        else:
            self.notification.close()
            self.notification.update('NOT OK TO TALK', '', 'r.jpg')
            self.notification.set_timeout(5*60*1000)
            self.notification.show()


if __name__ == "__main__":
    event_handler = PythonPatternHandler()
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
