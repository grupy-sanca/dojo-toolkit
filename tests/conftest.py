from unittest import mock

import pytest

from dojo_toolkit.code_handler import DojoCodeHandler
from dojo_toolkit.notifier import GnomeNotifier


@pytest.fixture
def mocked_code_handler():
    code_handler = DojoCodeHandler(notifier=mock.Mock(),
                                   test_runner=mock.Mock(),
                                   sound_player=mock.Mock())
    return code_handler


@pytest.fixture
def gnome_notifier():
    return GnomeNotifier()


@pytest.fixture
def mocked_gnome_notifier():
    with mock.patch('dojo_toolkit.notifier.Notify') as mock_notify, \
         mock.patch('dojo_toolkit.notifier.GdkPixbuf') as gdk_pixbuf:
        gnome_notifier = GnomeNotifier()
        gnome_notifier.mock_notify = mock_notify
        gnome_notifier.mock_gdk_pixbuf = gdk_pixbuf
        return gnome_notifier
