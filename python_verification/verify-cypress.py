#! /usr/bin/env python_verification
"""
A skeleton python_verification script which reads from an input file,
writes to an output file and parses command line arguments
"""
from __future__ import print_function
import json
import sys
from datetime import datetime

from python_verification.parseArgs import parse_args


def main():
    args = parse_args(sys.argv[1:])

    report_file = args.input.name

    report_data = json.load(open(report_file, 'r'))
    pass_percent = report_data["stats"]["passPercent"]
    start_time = datetime.fromisoformat(report_data["stats"]["start"])

    if pass_percent != 100:
        raise ValueError("Pass Percent is not 100%")
    if start_time.date() < datetime.utcnow().date():
        raise ValueError("Looks like tests weren't ran today")
    else:
        print("Cypress Test Status: {}% @ {} from input '{}'".format(pass_percent, start_time, report_file))


if __name__ == "__main__":
    main()
