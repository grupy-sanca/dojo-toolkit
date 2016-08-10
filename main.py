#!/usr/bin/python
"""Usage: python main.py path/to/directory"""
import time
import sys
import threading

from pgi.repository import Notify, GdkPixbuf
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from subprocess import Popen

# in minutes
round_time = 5

Notify.init('not')
notification = Notify.Notification.new('', '', '')
red = GdkPixbuf.Pixbuf.new_from_file("r.jpg")
green = GdkPixbuf.Pixbuf.new_from_file("g.jpg")


class PythonPatternHandler(PatternMatchingEventHandler):
    """Handles the python file changes"""
    global notification
    global red
    global green
    patterns = ['*.py']
    ignore_directories = True
    last_time = time.time()

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
        print("\033c")
        process = Popen([cmd], shell=True)
        process.wait()
        if process.returncode == 0:
            notification.update('OK TO TALK', '', 'g.jpg')
            notification.set_image_from_pixbuf(green)
            print('Tests passing!')
        else:
            notification.update('NOT OK TO TALK', '', 'r.jpg')
            notification.set_image_from_pixbuf(red)
        notification.set_timeout(5*60*1000)
        notification.show()


def dojo_timer(e):
    """Wait the defined and then shows notification and waits
    for replace
    """
    global notification
    global round_time
    global red
    global green
    while True:
        notification.update('Time Up', '', '')
        notification.set_timeout(15*1000)
        notification.show()
        print("\033c")
        input('Press Enter when replaced')
        time.sleep(round_time*60)


if __name__ == "__main__":
    event_handler = PythonPatternHandler()
    observer = Observer()
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print('Path to watch: {}\nTo change, reopen with path in first argument'.format(path))
    timer_event = threading.Event()
    timer_thread = threading.Thread(target=dojo_timer, args=(timer_event, ))
    timer_thread.start()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
