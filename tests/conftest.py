from unittest import mock

import pytest

from dojo_toolkit.code_handler import DojoCodeHandler


@pytest.fixture
def mocked_code_handler():
    code_handler = DojoCodeHandler(test_runner=mock.Mock(), dojo=mock.Mock())
    return code_handler
