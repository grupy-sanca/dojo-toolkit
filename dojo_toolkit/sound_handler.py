import os

import pyglet

from .settings import SOUNDS_DIR


class SoundHandler:
    def __init__(self):
        self.success_sound_path = os.path.join(SOUNDS_DIR, 'pass.wav')
        self.timeup_sound_path = os.path.join(SOUNDS_DIR, 'timeup.wav')
        self.start_sound_path = os.path.join(SOUNDS_DIR, 'start.wav')

    def play_sound(self, sound_path=''):
        self.player = pyglet.media.load(sound_path, streaming=False)
        self.player.play()

    def play_start(self):
        self.play_sound(self.start_sound_path)

    def play_timeup(self):
        self.play_sound(self.timeup_sound_path)

    def play_success(self):
        self.play_sound(self.success_sound_path)
