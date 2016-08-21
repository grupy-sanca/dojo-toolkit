import pytest

from dojo_toolkit.notifier import GnomeNotifier


@pytest.fixture
def gnome_notifier():
    return GnomeNotifier()
