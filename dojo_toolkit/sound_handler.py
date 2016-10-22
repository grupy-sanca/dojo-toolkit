import os

import pyglet

from .settings import SOUNDS_DIR
from .utils import mock


class SoundHandler:
    def __init__(self):
        # workaround to dojo-toolkit work on travis CI
        try:
            self.player = pyglet.media.Player()
        except:
            self.player = mock.Mock()

        start_audio_path = os.path.join(SOUNDS_DIR, 'start.wav')
        self.start_media = pyglet.media.load(start_audio_path, streaming=False)

        success_audio_path = os.path.join(SOUNDS_DIR, 'pass.wav')
        self.success_media = pyglet.media.load(success_audio_path, streaming=False)

        timeup_audio_path = os.path.join(SOUNDS_DIR, 'timeup.wav')
        self.timeup_media = pyglet.media.load(timeup_audio_path, streaming=False)

    def play(self):
        if self.player.playing:
            self.player.next_source()
        else:
            self.player.play()

    def play_start(self):
        self.player.queue(self.start_media)
        self.play()

    def play_success(self):
        self.player.queue(self.success_media)
        self.play()

    def play_timeup(self):
        self.player.queue(self.timeup_media)
        self.play()
