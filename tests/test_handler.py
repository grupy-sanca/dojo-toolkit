from unittest import mock

from dojo_toolkit.code_handler import DojoCodeHandler


def test_code_handler():
    code_handler = DojoCodeHandler(test_runner=mock.Mock(), dojo=mock.Mock())
    assert code_handler.last_test_run_time


def test_code_handler_get_last_test_run_interval(mocked_code_handler):
    mocked_code_handler.last_test_run_time = 10
    with mock.patch('time.time') as time:
        time.return_value = 20
        assert mocked_code_handler.get_last_test_run_interval() == 10


@mock.patch('dojo_toolkit.code_handler.DojoCodeHandler.get_last_test_run_interval')
def test_code_handler_on_modified(get_interval, mocked_code_handler):
    mocked_code_handler.test_runner.run.return_value = True
    get_interval.return_value = 10

    mocked_code_handler.on_modified(mock.Mock())

    assert get_interval.called
    assert mocked_code_handler.test_runner.run.called


@mock.patch('dojo_toolkit.code_handler.DojoCodeHandler.get_last_test_run_interval')
def test_code_handler_on_modified_on_short_interval(get_interval, mocked_code_handler):
    mocked_code_handler.test_runner.run.return_value = True
    get_interval.return_value = 1

    mocked_code_handler.on_modified(mock.Mock())

    assert get_interval.called
    assert not mocked_code_handler.test_runner.run.called


@mock.patch('dojo_toolkit.code_handler.DojoCodeHandler.get_last_test_run_interval')
def test_code_handler_on_modified_tests_fail(get_interval, mocked_code_handler):
    mocked_code_handler.test_runner.run.return_value = False
    get_interval.return_value = 10

    mocked_code_handler.on_modified(mock.Mock())

    assert get_interval.called
    assert mocked_code_handler.test_runner.run.called


@mock.patch('dojo_toolkit.code_handler.notifier')
def test_code_handler_handle_stopped_round(notifier, mocked_code_handler):
    mocked_code_handler.handle_stopped_round()
    assert notifier.notify.called
