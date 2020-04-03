from unittest import mock

from dojo_toolkit.__main__ import parse_args


@mock.patch('dojo_toolkit.__main__.ArgumentParser')
def test_main_parse_args(argument_parser):
    assert parse_args()
    assert argument_parser.called
