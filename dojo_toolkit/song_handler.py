import os

import vlc

from .settings import SONGS_DIR


class SongHandler:
    def __init__(self):
        self.success_song_path = os.path.join(SONGS_DIR, 'pass.mp3')
        self.timeup_song_path = os.path.join(SONGS_DIR, 'timeup.mp3')
        self.start_song_path = os.path.join(SONGS_DIR, 'start.mp3')

    def play_song(self, song_path=''):
        self.player = vlc.MediaPlayer(song_path)
        self.player.play()

    def play_start(self):
        self.play_song(self.start_song_path)

    def play_timeup(self):
        self.play_song(self.timeup_song_path)

    def play_success(self):
        self.play_song(self.success_song_path)
