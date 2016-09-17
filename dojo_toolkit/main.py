import argparse
import os
from dojo_toolkit.dojo import Dojo

ROUND_TIME = 5


def parse_args():
    """
    build argument parser
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time",
                        help="dojo time",
                        default=ROUND_TIME,
                        type=float)
    parser.add_argument("path",
                        help="code path",
                        nargs="?",
                        default=".",
                        type=os.path.realpath)

    return parser.parse_args()


def main():
    args = parse_args()
    dojo = Dojo(args.path, args.time)
    dojo.start()
