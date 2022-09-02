import sys
from threading import Thread
from unittest import mock

from watchdog.observers import Observer

from dojo_toolkit import dojo_thread
from dojo_toolkit.code_handler import DojoCodeHandler
from dojo_toolkit.sound_handler import SoundHandler
from dojo_toolkit.test_runner import get_test_runner
from dojo_toolkit.timer import Timer


class Dojo:
    ROUND_TIME = 5

    def __init__(self, code_path, round_time=None, mute=False, test_runner=None, runner="doctest"):
        self.code_path = code_path
        self.round_time = round_time or self.ROUND_TIME
        self.sound_player = mock.Mock() if mute or sys.platform != "linux" else SoundHandler()
        self.info_notified = False
        self.timer = Timer(self.round_time)

        test_runner = get_test_runner(test_runner, runner, self.code_path, self.sound_player)
        self.controller = dojo_thread.DojoController(self.timer, self.sound_player)

        event_handler = DojoCodeHandler(dojo=self.controller, test_runner=test_runner)

        self.observer = Observer()
        self.observer.schedule(event_handler, self.code_path, recursive=False)

    def start(self):
        self.observer.start()
        print("\nWatching: {} folder".format(self.code_path))

        self.is_running = True
        print("Dojo toolkit started!")
        self.thread = Thread(target=dojo_thread.main, args=(self.controller,))
        self.thread.daemon = True
        self.thread.start()

        self.thread.join()
        self.observer.join()
