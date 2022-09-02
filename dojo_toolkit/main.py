from enum import Enum
from pathlib import Path
from typing import Optional

import typer

from dojo_toolkit.dojo import Dojo


class Runners(str, Enum):
    doctest = "doctest"
    pytest = "pytest"


def main(
    path: Optional[Path] = typer.Argument(
        Path("."),
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        help="The path to the folder containing the code used during the dojo",
    ),
    time: Optional[float] = typer.Option(
        Dojo.ROUND_TIME,
        "--time",
        "-t",
        help="The amount of time a dojo round lasts",
    ),
    mute: Optional[bool] = typer.Option(
        False,
        help="Mute all sounds, note: this only works in Linux",
    ),
    runner: Optional[Runners] = typer.Option(
        Runners.doctest.value,
        "--runner",
        help="Name of the runner",
    ),
):
    dojo = Dojo(
        code_path=path.as_posix(),  # type: ignore
        round_time=time,  # type: ignore
        mute=mute,  # type: ignore
        runner=runner.value,  # type: ignore
    )
    dojo.start()


def run():
    typer.run(main)
