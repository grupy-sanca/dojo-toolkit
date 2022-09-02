from unittest import mock

import pytest

from dojo_toolkit.dojo import Dojo  # NOQA


@pytest.fixture
def mocked_dojo():
    with mock.patch("dojo_toolkit.dojo.Observer"), mock.patch(
        "dojo_toolkit.dojo.Timer"
    ), mock.patch("dojo_toolkit.dojo.SoundHandler"):
        return Dojo("/foo/bar", test_runner=mock.Mock())


@mock.patch("dojo_toolkit.dojo.Thread")
@mock.patch("dojo_toolkit.dojo.input")
def test_dojo_start(input, thread, mocked_dojo):
    mocked_dojo.start()

    assert mocked_dojo.observer.start.called
    assert mocked_dojo.thread.start.called
    assert mocked_dojo.thread.join.called
    assert mocked_dojo.observer.join.called
