import sys
import time
import threading

from watchdog.observers import Observer

from dojo_toolkit.code_handler import DojoCodeHandler
from dojo_toolkit.notifier import GnomeNotifier
from dojo_toolkit.test_runner import DoctestTestRunner
from dojo_toolkit.timer import dojo_timer


class Dojo:
    def __init__(self, code_path, round_time=5, notifier=None, test_runner=None):
        print('Watching: {}\nTo change, reopen with path in first argument'.format(code_path))

        self.round_time = round_time

        if not notifier:
            notifier = GnomeNotifier()

        if not test_runner:
            test_runner = DoctestTestRunner(code_path=code_path)

        self.event_handler = DojoCodeHandler(notifier=notifier, test_runner=test_runner)
        self.observer = Observer()
        self.observer.schedule(self.event_handler, code_path, recursive=False)

        self.timer_thread = threading.Thread(target=dojo_timer, args=(notifier, self.round_time))

    def start(self):
        self.observer.start()
        self.timer_thread.start()
        try:
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


def main():
    code_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    dojo = Dojo(code_path)
    dojo.start()


if __name__ == "__main__":
    main()
