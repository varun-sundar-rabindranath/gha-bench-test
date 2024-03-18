# store a benchmark jsons

from pathlib import Path
import json
import argparse
import random


def main(out_file, metric_type):

    dicts = []
    if metric_type == 'customBiggerIsBetter':
        dicts.append({
            "name": "bigger_is_better",
            "unit": "ms",
            "value": 120})
    elif metric_type == 'customSmallerIsBetter':
        dicts.append({
            "name": "smaller_is_better",
            "unit": "ms",
            "value": 120})

    with open(out_file, "w+") as f:
        json.dump(dicts, f, sort_keys=True, indent=4)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
    description="dumps a bench json")

    parser.add_argument(
          "-t",
          "--type",
          type=str,
          default=None,
          required=True,
          help="type of metrics")

    parser.add_argument(
          "-o",
          "--output-file",
          type=str,
          default=None,
          required=True,
          help="Path to a file where the output json is stored")

    args = parser.parse_args()
    main(Path(args.output_file), args.type)
