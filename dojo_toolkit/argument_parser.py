import doctest
import argparse
import os

ROUND_TIME = 5


def build_parser():
    """
    build argument parser
    >>> args = "-p /must/have/a/path".split()
    >>> build_parser().parse_args(args)
    Namespace(path='/must/have/a/path', time=5)

    >>> args = "-p /must/have/a/path -t 5.1".split()
    >>> build_parser().parse_args(args)
    Namespace(path='/must/have/a/path', time=5.1)

    >>> build_parser().parse_args([]) # missing -p
    Traceback (most recent call last):
    ...
    SystemExit: 2
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path",
                        required=True,
                        help="code path",
                        type=os.path.realpath)

    parser.add_argument("-t", "--time",
                        help="dojo time",
                        default=ROUND_TIME,
                        type=float)

    return parser


doctest.testmod()
