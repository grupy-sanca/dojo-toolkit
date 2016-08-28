from unittest import mock

from dojo_toolkit.dojo import Dojo


def test_dojo():
    dojo = Dojo('/foo/bar', notifier=mock.Mock(), test_runner=mock.Mock())
    assert dojo.round_time
    assert dojo.event_handler
    assert dojo.observer
    assert dojo.timer_thread


@mock.patch('threading.Thread')
@mock.patch('dojo_toolkit.dojo.dojo_timer')
@mock.patch('dojo_toolkit.dojo.Observer')
@mock.patch('dojo_toolkit.dojo.SoundHandler')
def test_dojo_start(observer, dojo_timer, sound_handler, thread):
    dojo = Dojo('/foo/bar')
    with mock.patch('time.sleep', side_effect=KeyboardInterrupt):
        dojo.start()

    assert dojo_timer.called
    assert dojo.sound_player.play_start.called
    assert dojo.timer_thread.start.called
    assert dojo.observer.schedule.called
    assert dojo.observer.start.called
    assert dojo.observer.stop.called
    assert dojo.observer.join.called
