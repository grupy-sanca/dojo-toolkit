from unittest import mock

from dojo_toolkit.main import parse_args


@mock.patch("dojo_toolkit.main.ArgumentParser")
def test_main_parse_args(argument_parser):
    assert parse_args()
    assert argument_parser.called
