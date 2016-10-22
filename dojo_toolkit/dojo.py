from threading import Thread

from six import moves
from watchdog.observers import Observer

from dojo_toolkit.code_handler import DojoCodeHandler
from dojo_toolkit.notifier import GnomeNotifier
from dojo_toolkit.sound_handler import SoundHandler
from dojo_toolkit.test_runner import DoctestTestRunner
from dojo_toolkit.timer import Timer
from dojo_toolkit.utils import mock


class Dojo:
    ROUND_TIME = 5

    def __init__(self, code_path, round_time=None, mute=False, notifier=None, test_runner=None):
        self.code_path = code_path
        self.round_time = round_time or self.ROUND_TIME
        self.notifier = notifier or GnomeNotifier()
        self.test_runner = test_runner or DoctestTestRunner(code_path=code_path)
        self.sound_player = mock.Mock() if mute else SoundHandler()

        self.event_handler = DojoCodeHandler(notifier=self.notifier,
                                             test_runner=self.test_runner,
                                             sound_player=self.sound_player)
        self.observer = Observer()
        self.observer.schedule(self.event_handler, self.code_path, recursive=False)

        self.timer = Timer(self.round_time)

    def start(self):
        self.observer.start()
        print('\n\n\n\nWatching: {} folder'.format(self.code_path))

        self.is_running = True
        print('Dojo toolkit started!')
        self.thread = Thread(target=self.dojo)
        self.thread.start()

        self.thread.join()
        self.observer.join()

    def stop(self):
        self.is_running = False

    def await_pilot_exchange(self):
        moves.input()

    def round_start(self):
        self.timer.start()
        self.sound_player.play_start()

    def round_info(self):
        if self.timer.ellapsed_time == 60:
            self.notifier.notify('60 seconds...')
            print('Round finished in 60 seconds')

    def round_finished(self):
        self.notifier.notify('Time Up', timeout=15 * 1000)
        self.sound_player.play_timeup()

    def dojo(self):
        while self.is_running:
            print('Awaiting the pilot and co-pilot to enter their positions.')
            print('Press <Enter> when they are ready')
            self.await_pilot_exchange()
            self.round_start()
            print('Round started! {} minutes left...'.format(self.round_time))
            while self.timer.is_running:
                self.round_info()
            self.round_finished()
            print('Round finished!')
