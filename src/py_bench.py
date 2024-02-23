# store a benchmark jsons

from pathlib import Path
import json
import argparse
import random


def main(out_file):

    dicts = []
    dicts.append({
        "name": "My Custom Smaller Is Better Benchmark - Dummy 1",
        "unit": "Percent",
        "value": f"{random.randint(10, 100)}"})
    dicts.append({
        "name": "My Custom Smaller Is Better Benchmark - Dummy 2",
        "unit": "Megabytes",
        "value": f"{random.randint(10, 100)}",
        "range": "3",
        "extra": "Value for Tooltip: 25\nOptional Num #2: 100\nAnything Else!"
    })

    with open(out_file, "w+") as f:
        json.dump(dicts, f, sort_keys=True, indent=4)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
    description="dumps a bench json")

    parser.add_argument(
          "-o",
          "--output-file",
          type=str,
          default=None,
          required=True,
          help="Path to a file where the output json is stored")

    args = parser.parse_args()
    main(Path(args.output_file))
