from unittest import mock

import pytest

from dojo_toolkit.dojo_thread import DojoController, main


@pytest.fixture
def dojo_controller():
    timer_mock = mock.Mock()
    sound_handler_mock = mock.Mock()
    timer_mock.duration = 10
    return DojoController(timer_mock, sound_handler_mock)


@mock.patch("dojo_toolkit.dojo_thread.DojoController.await_pilot_exchange")
@mock.patch("dojo_toolkit.dojo_thread.time")
def test_dojo_thread(time_mock, await_pilot_exchange_mock, dojo_controller):
    dojo_controller.is_running = True
    dojo_controller.timer.is_running = False
    dojo_controller.round_finished = mock.Mock(side_effect=KeyboardInterrupt)
    with pytest.raises(KeyboardInterrupt):
        main(dojo_controller)


@mock.patch("dojo_toolkit.dojo_thread.DojoController.await_pilot_exchange")
@mock.patch("dojo_toolkit.dojo_thread.time")
def test_dojo_timer_running(time_mock, await_pilot_exchange_mock, dojo_controller):
    dojo_controller.is_running = True
    dojo_controller.timer.is_running = True

    def stop_dojo():
        dojo_controller.is_running = False

    def stop_timer():
        dojo_controller.timer.is_running = False

    dojo_controller.round_info = mock.Mock(side_effect=stop_timer)
    dojo_controller.round_finished = mock.Mock(side_effect=stop_dojo)
    main(dojo_controller)


def test_dojo_stopped():
    dojo_controller = mock.MagicMock(spec=DojoController)
    dojo_controller.is_running = False
    main(dojo_controller)
    dojo_controller.await_pilot_exchange.assert_not_called()
    dojo_controller.round_start.assert_not_called()
    dojo_controller.round_info.assert_not_called()
    dojo_controller.round_finished.assert_not_called()


@mock.patch("dojo_toolkit.dojo_thread.input")
def test_dojo_await_pilot_exchange(mock_input, dojo_controller):
    dojo_controller.await_pilot_exchange()
    mock_input.assert_called_once_with()


def test_dojo_round_start(dojo_controller):
    assert dojo_controller.round_started is False

    dojo_controller.round_start()

    assert dojo_controller.timer.start.called
    assert dojo_controller.sound_player.play_start.called
    assert dojo_controller.round_started is True


@mock.patch("dojo_toolkit.dojo_thread.notifier")
def test_dojo_round_info_without_notification(notifier, dojo_controller):
    dojo_controller.round_info()
    notifier.notify.assert_not_called()


@mock.patch("dojo_toolkit.dojo_thread.notifier")
def test_dojo_round_info_with_notification(notifier, dojo_controller):
    dojo_controller.timer.duration = 120
    dojo_controller.timer.elapsed_time = 60
    dojo_controller.round_info()
    assert notifier.notify.called


@mock.patch("dojo_toolkit.dojo_thread.notifier")
def test_dojo_round_finished(notifier, dojo_controller):
    dojo_controller.round_started = True

    dojo_controller.round_finished()

    assert notifier.notify.called
    dojo_controller.sound_player.play_timeup.assert_called_once_with()
    assert dojo_controller.round_started is False
