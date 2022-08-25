from unittest import mock

import typer
from typer.testing import CliRunner

from dojo_toolkit.main import main, run

app = typer.Typer()
app.command()(main)
runner = CliRunner()


@mock.patch("dojo_toolkit.main.Dojo")
def test_main(mock_dojo):
    result = runner.invoke(app)
    assert result.exit_code == 0
    mock_dojo.assert_called_once_with(
        code_path=".",
        round_time=5.0,
        mute=False,
        runner="doctest",
    )
    mock_dojo.return_value.start.assert_called_once_with()


@mock.patch("dojo_toolkit.main.typer")
def test_run(mock_typer):
    run()
    mock_typer.run.assert_called_once_with(main)
