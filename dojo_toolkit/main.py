import os
from argparse import ArgumentParser

from dojo_toolkit.dojo import Dojo


def parse_args():
    """
    build argument parser
    """
    parser = ArgumentParser()
    parser.add_argument(
        "-t",
        "--time",
        help="the amount of time a dojo round lasts",
        default=Dojo.ROUND_TIME,
        type=float,
    )
    parser.add_argument(
        "path",
        help="the path to the folder containing the code used during the dojo",
        nargs="?",
        default=".",
        type=os.path.realpath,
    )
    parser.add_argument(
        "--mute",
        help="mute all sounds (default: all sounds are played), note: this only works in Linux",
        action="store_true",
    )
    parser.add_argument(
        "--runner", help="name of the runner (default: doctest)", default="doctest", type=str
    )

    return parser.parse_args()


def main():
    args = parse_args()
    dojo = Dojo(code_path=args.path, round_time=args.time, mute=args.mute, runner=args.runner)
    dojo.start()
