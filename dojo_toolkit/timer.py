import time
from math import floor
from threading import Thread


class Timer:
    """
    A timer that runs on a separated thread and "ticks" every second. It
    keeps track of the elapsed time.
    """

    def __init__(self, duration_in_minutes):
        self.duration = duration_in_minutes * 60

    def start(self):
        self.elapsed_time = 0

        self.is_running = True
        self.start_time = time.time()

        self.thread = Thread(target=self.timer)
        self.thread.start()

    def timer(self):
        while self.elapsed_time <= self.duration:
            self.elapsed_time = floor(time.time() - self.start_time)
            time.sleep(1)
        self.is_running = False
