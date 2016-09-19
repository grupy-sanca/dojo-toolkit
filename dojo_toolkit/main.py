import argparse
import os
from dojo_toolkit.dojo import Dojo


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--time",
                        help="the amount of time a dojo round lasts",
                        default=Dojo.ROUND_TIME,
                        type=float)

    parser.add_argument("path",
                        help="the path to the _folder_ containing the code",
                        nargs="?",
                        default=".",
                        type=os.path.realpath)

    parser.add_argument("--mute",
                        help="mute all sounds (default: all sounds are played)",
                        action='store_true')

    return parser.parse_args()


def main():
    args = parse_args()
    dojo = Dojo(code_path=args.path,
                round_time=args.time,
                mute_sound=args.mute)
    dojo.start()
