from unittest import mock

from dojo_toolkit.notifier import Notifier


@mock.patch("desktop_notifier.sync.DesktopNotifierSync.send")
def test_notifyier(send):
    n = Notifier()
    n.notify("message")
    assert send.call_args_list == [mock.call(title='dojo toolkit', message='message', timeout=300)]
