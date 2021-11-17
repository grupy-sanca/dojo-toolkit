import sys
import time
from threading import Thread
from unittest import mock

from clint.textui import colored
from watchdog.observers import Observer

from dojo_toolkit.code_handler import DojoCodeHandler
from dojo_toolkit.notifier import notifier
from dojo_toolkit.sound_handler import SoundHandler
from dojo_toolkit.test_runner import get_test_runner
from dojo_toolkit.timer import Timer


class Dojo:
    ROUND_TIME = 5
    round_started = False

    def __init__(self, code_path, round_time=None, mute=False, test_runner=None, runner="doctest"):
        self.code_path = code_path
        self.round_time = round_time or self.ROUND_TIME
        self.sound_player = mock.Mock() if mute or sys.platform != "linux" else SoundHandler()
        self.info_notified = False

        test_runner = get_test_runner(test_runner, runner, self.code_path, self.sound_player)

        event_handler = DojoCodeHandler(dojo=self, test_runner=test_runner)

        self.observer = Observer()
        self.observer.schedule(event_handler, self.code_path, recursive=False)

        self.timer = Timer(self.round_time)

    def start(self):
        self.observer.start()
        print("\nWatching: {} folder".format(self.code_path))

        self.is_running = True
        print("Dojo toolkit started!")
        self.thread = Thread(target=self.dojo)
        self.thread.start()

        self.thread.join()
        self.observer.join()

    def stop(self):
        self.is_running = False

    def await_pilot_exchange(self):
        print("Awaiting the pilot and co-pilot to enter their positions.")
        print("Press <Enter> when they are ready")
        input()

    def round_start(self):
        self.timer.start()
        self.sound_player.play_start()
        self.round_started = True
        self.info_notified = False

        print("Round started! {} minutes left...".format(self.round_time))

    def round_info(self):
        if self.timer.ellapsed_time == self.timer.duration - 60 and not self.info_notified:
            notifier.notify("60 seconds to round finish...")
            print((getattr(colored, "yellow"))("Round is going to finish in 60 seconds"))
            self.info_notified = True

    def round_finished(self):
        notifier.notify("Time Up", timeout=15 * 1000)
        self.sound_player.play_timeup()
        self.round_started = False
        print("Round finished!\n")

    def dojo(self):
        while self.is_running:
            self.await_pilot_exchange()
            self.round_start()
            while self.timer.is_running:
                self.round_info()
                time.sleep(0.8)
            self.round_finished()
