from dojo_toolkit.main import main, parse_args
from dojo_toolkit.utils import mock


@mock.patch('dojo_toolkit.main.ArgumentParser')
def test_main_parse_args(argument_parser):
    assert parse_args()
    assert argument_parser.called


@mock.patch('dojo_toolkit.main.ArgumentParser')
@mock.patch('dojo_toolkit.main.Dojo')
def test_main_main(dojo, argparser):
    main()
    assert dojo.called
