import time
from dataclasses import dataclass

from clint.textui import colored

from dojo_toolkit.notifier import notifier
from dojo_toolkit.sound_handler import SoundHandler
from dojo_toolkit.timer import Timer


@dataclass
class DojoController:
    timer: Timer
    sound_player: SoundHandler
    is_running: bool = True
    round_started: bool = False
    info_notified: bool = False

    def await_pilot_exchange(self):
        print("Awaiting the pilot and co-pilot to enter their positions.")
        print("Press <Enter> when they are ready")
        input()
        print("Starting round...")

    def round_start(self):
        self.timer.start()
        self.sound_player.play_start()
        self.round_started = True
        self.info_notified = False

    def round_info(self):
        if self.timer.elapsed_time == self.timer.duration - 60 and not self.info_notified:
            notifier.notify("60 seconds to round finish...")
            print((getattr(colored, "yellow"))("Round is going to finish in 60 seconds"))
            self.info_notified = True

    def round_finished(self):
        notifier.notify("Time Up", timeout=15 * 1000)
        self.sound_player.play_timeup()
        self.round_started = False
        print("Round finished!\n")


def main(controller: DojoController):
    while controller.is_running:
        controller.await_pilot_exchange()
        controller.round_start()
        while controller.timer.is_running:
            controller.round_info()
            time.sleep(0.8)
        controller.round_finished()
