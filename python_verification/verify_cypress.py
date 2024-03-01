import argparse
import json
from datetime import datetime


def inspect_report(args):
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "input", nargs="?", default="-",
        metavar="INPUT_FILE", type=argparse.FileType("r"),
        help="path to the input file (read from stdin if omitted)")

    inputs = parser.parse_args(args)

    with open(inputs.input.name, 'r') as file:
        report_data = json.load(file)
        pass_percent = report_data["stats"]["passPercent"]
        start_time = datetime.fromisoformat(report_data["stats"]["start"])

        if pass_percent != 100:
            raise ValueError("Pass Percent is not 100%")
        if start_time.date() < datetime.utcnow().date():
            raise ValueError("Looks like tests weren't ran today")
        else:
            print("Cypress Test Status: {}% @ {} from input '{}'".format(pass_percent, start_time, inputs.input.name))
            return True
