from enum import Enum
from pathlib import Path
from typing import Annotated, Optional

import typer

from dojo_toolkit.dojo import Dojo


class Runners(str, Enum):
    doctest = "doctest"
    pytest = "pytest"


def main(
    path: Annotated[
        Optional[Path],
        typer.Argument(
            exists=True,
            file_okay=False,
            dir_okay=True,
            readable=True,
            help="The path to the folder containing the code used during the dojo",
        ),
    ] = Path("."),
    time: Annotated[
        Optional[float],
        typer.Option(
            "--time",
            "-t",
            help="The amount of time a dojo round lasts",
        ),
    ] = Dojo.ROUND_TIME,
    mute: Annotated[
        Optional[bool],
        typer.Option(
            help="Mute all sounds, note: this only works in Linux",
        ),
    ] = False,
    runner: Annotated[
        Optional[Runners],
        typer.Option(
            "--runner",
            help="Name of the runner",
        ),
    ] = Runners.doctest,
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
