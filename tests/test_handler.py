from tests.conftest import mock


def test_code_handler_get_last_test_run_interval(mocked_code_handler):
    mocked_code_handler.last_test_run_time = 10
    with mock.patch('time.time') as time:
        time.return_value = 20
        assert mocked_code_handler.get_last_test_run_interval() == 10


def test_code_handler_handle_success(mocked_code_handler):
    mocked_code_handler.handle_success()

    assert mocked_code_handler.notifier.success.called
    assert mocked_code_handler.sound_player.play_success.called


def test_code_handler_handle_fail(mocked_code_handler):
    mocked_code_handler.handle_fail()

    assert mocked_code_handler.notifier.fail.called


def test_code_handler_handle_stopped_round(mocked_code_handler):
    mocked_code_handler.handle_stopped_round()

    assert mocked_code_handler.notifier.notify.called


@mock.patch('dojo_toolkit.code_handler.DojoCodeHandler.handle_success')
@mock.patch('dojo_toolkit.code_handler.DojoCodeHandler.get_last_test_run_interval')
def test_code_handler_on_modified(get_interval, handle_success, mocked_code_handler):
    mocked_code_handler.test_runner.run.return_value = True
    get_interval.return_value = 10

    mocked_code_handler.on_modified(mock.Mock())

    assert get_interval.called
    assert mocked_code_handler.test_runner.run.called
    assert handle_success.called


@mock.patch('dojo_toolkit.code_handler.DojoCodeHandler.handle_success')
@mock.patch('dojo_toolkit.code_handler.DojoCodeHandler.get_last_test_run_interval')
def test_code_handler_on_modified_on_short_interval(get_interval, handle_success,
                                                    mocked_code_handler):
    mocked_code_handler.test_runner.run.return_value = True
    get_interval.return_value = 1

    mocked_code_handler.on_modified(mock.Mock())

    assert get_interval.called
    assert not mocked_code_handler.test_runner.run.called
    assert not handle_success.called


@mock.patch('dojo_toolkit.code_handler.DojoCodeHandler.handle_fail')
@mock.patch('dojo_toolkit.code_handler.DojoCodeHandler.get_last_test_run_interval')
def test_code_handler_on_modified_tests_fail(get_interval, handle_fail, mocked_code_handler):
    mocked_code_handler.test_runner.run.return_value = False
    get_interval.return_value = 10

    mocked_code_handler.on_modified(mock.Mock())

    assert get_interval.called
    assert mocked_code_handler.test_runner.run.called
    assert handle_fail.called
