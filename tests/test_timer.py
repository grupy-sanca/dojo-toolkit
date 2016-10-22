import pytest

from dojo_toolkit.timer import Timer
from dojo_toolkit.utils import mock


@pytest.fixture
def mocked_timer():
    return Timer(5)


@mock.patch('dojo_toolkit.timer.Thread')
@mock.patch('time.time')
def test_timer_start(time, thread, mocked_timer):
    mocked_timer.start()

    assert mocked_timer.ellapsed_time == 0
    assert mocked_timer.is_running is True
    assert time.called
    assert mocked_timer.thread.start.called


@mock.patch('time.sleep')
@mock.patch('time.time')
def test_timer_timer(time, sleep, mocked_timer):
    time.return_value = 11

    mocked_timer.ellapsed_time = 0
    mocked_timer.duration = 10
    mocked_timer.start_time = 0

    mocked_timer.timer()
    assert sleep.called
    assert time.called
    assert mocked_timer.is_running is False
