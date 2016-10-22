import pytest

from dojo_toolkit.notifier import BaseNotifier, GnomeNotifier
from dojo_toolkit.utils import mock


@pytest.fixture
def gnome_notifier():
    return GnomeNotifier()


def test_base_notifier():
    notifier = BaseNotifier()
    assert notifier.fail_img_path
    assert notifier.success_img_path
    with pytest.raises(NotImplementedError):
        notifier.notify('foo')
    with pytest.raises(NotImplementedError):
        notifier.get_notifier()


@mock.patch('dojo_toolkit.notifier.Notify')
@mock.patch('dojo_toolkit.notifier.GdkPixbuf')
def test_gnome_notifier(pixbuf, notify):
    gnome_notifier = GnomeNotifier()

    calls = [
        mock.call(gnome_notifier.fail_img_path),
        mock.call(gnome_notifier.success_img_path)
    ]
    pixbuf.Pixbuf.new_from_file.assert_has_calls(calls)


@mock.patch('dojo_toolkit.notifier.Notify')
def test_gnome_notifier_get_notifier(notify, gnome_notifier):
    assert gnome_notifier.get_notifier()

    notify.init.assert_called_once_with('not')
    notify.Notification.new.assert_called_once_with('', '', '')


@mock.patch('dojo_toolkit.notifier.GnomeNotifier.get_notifier')
def test_gnome_notifier_notify(get_notifier, gnome_notifier):
    gnome_notifier = GnomeNotifier()

    gnome_notifier.notify('message', 'foo.png', 10)

    _notifier = get_notifier.return_value
    _notifier.update.assert_called_with('message', '', 'foo.png')
    _notifier.set_timeout.assert_called_with(10)
    assert _notifier.show.called


@mock.patch('dojo_toolkit.notifier.GnomeNotifier.notify')
def test_gnome_notifier_success(notify, gnome_notifier):
    gnome_notifier.success('message')
    notify.assert_called_with('message', gnome_notifier.success_img_path)


@mock.patch('dojo_toolkit.notifier.GnomeNotifier.notify')
def test_gnome_notifier_fail(notify, gnome_notifier):
    gnome_notifier.fail('message')
    notify.assert_called_with('message', gnome_notifier.fail_img_path)
