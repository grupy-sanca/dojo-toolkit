import os

import vlc

from .settings import SOUNDS_DIR


class SongHandler:
    def __init__(self):
        self.success_song_path = os.path.join(SOUNDS_DIR, 'pass.mp3')
        self.timeup_song_path = os.path.join(SOUNDS_DIR, 'timeup.mp3')
        self.start_song_path = os.path.join(SOUNDS_DIR, 'start.mp3')

    def play_song(self, sound_path=''):
        self.player = vlc.MediaPlayer(sound_path)
        self.player.play()

    def play_start(self):
        self.play_song(self.start_sound_path)

    def play_timeup(self):
        self.play_song(self.timeup_sound_path)

    def play_success(self):
        self.play_song(self.success_sound_path)
