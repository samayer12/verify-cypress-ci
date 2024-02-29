#! /usr/bin/env python
"""
A skeleton python script which reads from an input file,
writes to an output file and parses command line arguments
"""
from __future__ import print_function
import argparse
import json
from datetime import date, datetime, timezone


def main():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "input", nargs="?", default="-",
        metavar="INPUT_FILE", type=argparse.FileType("r"),
        help="path to the input file (read from stdin if omitted)")

    parser.add_argument(
        "output", nargs="?", default="-",
        metavar="OUTPUT_FILE", type=argparse.FileType("w"),
        help="path to the output file (write to stdout if omitted)")

    args = parser.parse_args()

    report_file = args.input.name
    output_file = args.output.name

    report_data = json.load(open(report_file, 'r'))
    pass_percent = report_data["stats"]["passPercent"]
    start_time = datetime.fromisoformat(report_data["stats"]["start"])

    print("Pass Percent: {} @ {}".format(pass_percent, start_time))
    if pass_percent != 100:
        raise ValueError("Pass Percent is not 100%")
    if start_time.date() < datetime.utcnow().date():
        raise ValueError("Looks like tests weren't ran today")

if __name__ == "__main__":
    main()
