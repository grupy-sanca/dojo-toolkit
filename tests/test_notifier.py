from unittest import mock

from dojo_toolkit.notifier import Notifier


@mock.patch("desktop_notifier.sync.DesktopNotifierSync.send")
def test_notifyier(send):
    n = Notifier()
    n.notify("a")
    n.success("b")
    n.fail("c")
    assert send.call_args_list == [
        mock.call(title='dojo toolkit', message='a', timeout=300),
        mock.call(title='dojo success', message='b', icon=n.SUCCESS_ICON),
        mock.call(title='dojo fail', message='c', icon=n.FAIL_ICON)
    ]
