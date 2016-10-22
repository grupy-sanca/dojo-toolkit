import pytest

from dojo_toolkit.dojo import Dojo  # NOQA
from dojo_toolkit.utils import mock


@pytest.fixture
def mocked_dojo():
    with mock.patch('dojo_toolkit.dojo.Observer'), \
            mock.patch('dojo_toolkit.dojo.Timer'), \
            mock.patch('dojo_toolkit.dojo.SoundHandler'):
        return Dojo('/foo/bar', notifier=mock.Mock(), test_runner=mock.Mock())


@mock.patch('dojo_toolkit.dojo.Thread')
@mock.patch('six.moves.input')
def test_dojo_start(input, thread, mocked_dojo):
    mocked_dojo.start()

    assert mocked_dojo.observer.start.called
    assert mocked_dojo.thread.start.called
    assert mocked_dojo.thread.join.called
    assert mocked_dojo.observer.join.called


@mock.patch('six.moves.input')
def test_dojo_dojo(input, mocked_dojo):
    mocked_dojo.is_running = True
    mocked_dojo.timer.is_running = False
    mocked_dojo.round_finished = mock.Mock(side_effect=KeyboardInterrupt)
    with pytest.raises(KeyboardInterrupt):
        mocked_dojo.dojo()


@mock.patch('six.moves.input')
def test_dojo_dojo_timer_running(input, mocked_dojo):
    mocked_dojo.is_running = True
    mocked_dojo.timer.is_running = True

    def stop_dojo():
        mocked_dojo.is_running = False

    def stop_timer():
        mocked_dojo.timer.is_running = False

    mocked_dojo.round_info = mock.Mock(side_effect=stop_timer)
    mocked_dojo.round_finished = mock.Mock(side_effect=stop_dojo)
    mocked_dojo.dojo()


def test_dojo_dojo_stopped(mocked_dojo):
    mocked_dojo.is_running = False
    mocked_dojo.dojo()


@mock.patch('six.moves.input')
def test_dojo_await_pilot_exchange(six_input, mocked_dojo):
    mocked_dojo.await_pilot_exchange()
    assert six_input.called


def test_dojo_round_start(mocked_dojo):
    mocked_dojo.round_start()
    assert mocked_dojo.timer.start.called
    assert mocked_dojo.sound_player.play_start.called


def test_dojo_round_info_without_notification(mocked_dojo):
    mocked_dojo.round_info()
    assert not mocked_dojo.notifier.notify.called


def test_dojo_round_info_with_notification(mocked_dojo):
    mocked_dojo.timer.ellapsed_time = 60
    mocked_dojo.round_info()
    assert mocked_dojo.notifier.notify.called


def test_dojo_round_finished(mocked_dojo):
    mocked_dojo.round_finished()
    assert mocked_dojo.notifier.notify.called
    assert mocked_dojo.sound_player.play_timeup.called
