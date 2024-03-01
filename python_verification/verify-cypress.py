#! /usr/bin/env python_verification
"""
A skeleton python_verification script which reads from an input file,
writes to an output file and parses command line arguments
"""
from __future__ import print_function

import sys

import python_verification.parseArgs


def main():
    python_verification.parseArgs.inspect_report(sys.argv[1:])


if __name__ == "__main__":
    main()
