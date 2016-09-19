import pytest

from dojo_toolkit.sound_handler import MutedSoundHandler, SoundHandler
from tests.conftest import mock


@pytest.fixture
def mocked_sound_handler():
    with mock.patch('dojo_toolkit.sound_handler.pyglet'):
        return SoundHandler()


@pytest.fixture
def mocked_muted_sound_handler():
    with mock.patch('dojo_toolkit.sound_handler.pyglet'):
        return MutedSoundHandler()


def test_sound_handler_muted_sound_handler(mocked_muted_sound_handler):
    mocked_muted_sound_handler.play_start()
    mocked_muted_sound_handler.play_timeup()
    mocked_muted_sound_handler.play_success()


@mock.patch('dojo_toolkit.sound_handler.pyglet')
def test_sound_handler(pyglet):
    sound_handler = SoundHandler()
    assert sound_handler
    assert sound_handler.play_start
    assert sound_handler.play_timeup
    assert sound_handler.play_success


def test_sound_handler_play(mocked_sound_handler):
    mocked_sound_handler.player.playing = False
    mocked_sound_handler.play()

    assert mocked_sound_handler.player.play.called


def test_sound_handler_play_start(mocked_sound_handler):
    mocked_sound_handler.player.playing = True
    mocked_sound_handler.play_start()

    assert mocked_sound_handler.player.queue.called
    assert mocked_sound_handler.player.next_source.called


def test_sound_handler_play_success(mocked_sound_handler):
    mocked_sound_handler.play_success()

    assert mocked_sound_handler.player.queue.called
    assert mocked_sound_handler.player.next_source.called


def test_sound_handler_play_timeup(mocked_sound_handler):
    mocked_sound_handler.play_timeup()

    assert mocked_sound_handler.player.queue.called
    assert mocked_sound_handler.player.next_source.called
