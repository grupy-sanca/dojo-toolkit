import time
import threading

from watchdog.observers import Observer

from dojo_toolkit.code_handler import DojoCodeHandler
from dojo_toolkit.notifier import GnomeNotifier
from dojo_toolkit.test_runner import DoctestTestRunner
from dojo_toolkit.timer import dojo_timer
from dojo_toolkit.sound_handler import SoundHandler


class Dojo:
    ROUND_TIME = 5

    def __init__(self, code_path, round_time=None, notifier=None, test_runner=None,
                 mute_sound=False):
        print('Watching: {}\nTo change, reopen with path in first argument'.format(code_path))

        self.sound_player = SoundHandler(mute_sound)

        if not round_time:
            round_time = self.ROUND_TIME
        self.round_time = round_time

        if not notifier:
            notifier = GnomeNotifier()

        if not test_runner:
            test_runner = DoctestTestRunner(code_path=code_path)

        self.event_handler = DojoCodeHandler(notifier=notifier,
                                             test_runner=test_runner,
                                             sound_player=self.sound_player)
        self.observer = Observer()
        self.observer.schedule(self.event_handler, code_path, recursive=False)

        thread_args = (notifier, self.round_time, self.sound_player)
        self.timer_thread = threading.Thread(target=dojo_timer, args=thread_args)

    def start(self):
        self.observer.start()
        self.timer_thread.start()
        try:
            while True:
                time.sleep(0.5)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()
