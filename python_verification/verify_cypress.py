import argparse
import json
from datetime import datetime


TEST_STATUS_MESSAGE = "Cypress Test Status: {}% @ {} from input '{}'. "
PASS_THRESHOLD = 100


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

        if pass_percent != PASS_THRESHOLD:
            raise ValueError(
                TEST_STATUS_MESSAGE.format(pass_percent, start_time, inputs.input.name) +
                "Pass percentage is not {}.".format(PASS_THRESHOLD)
            )

        if start_time.date() < datetime.utcnow().date():
            raise ValueError(
                TEST_STATUS_MESSAGE.format(pass_percent, start_time, inputs.input.name) +
                "It looks like journey tests weren't ran today."
            )
        else:
            print(TEST_STATUS_MESSAGE.format(pass_percent, start_time, inputs.input.name))
            return True
