import pytest

from dojo_toolkit.code_handler import DojoCodeHandler
from dojo_toolkit.utils import mock


@pytest.fixture
def mocked_code_handler():
    code_handler = DojoCodeHandler(notifier=mock.Mock(),
                                   test_runner=mock.Mock(),
                                   sound_player=mock.Mock())
    return code_handler
