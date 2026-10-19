"""A first sports-analytics model: does shot distance predict goals?

Runs anywhere Python runs (or paste it to your AI and ask it to walk
you through). Uses NHSSAA's xG-for-beginners open shot data; swap in
any CSV with `distance` and `goal` columns to make it yours.
"""

import csv
import io
import urllib.request

DATA_URL = "https://raw.githubusercontent.com/nhssaa/xg-for-beginners/main/shots.csv"


def main():
    rows = list(csv.DictReader(io.StringIO(urllib.request.urlopen(DATA_URL).read().decode())))
    buckets = {"close (<10m)": [0, 0], "far (>=10m)": [0, 0]}
    for r in rows:
        key = "close (<10m)" if float(r["distance"]) < 10 else "far (>=10m)"
        buckets[key][0] += int(r["goal"])
        buckets[key][1] += 1
    for key, (goals, shots) in buckets.items():
        print(f"{key}: {goals}/{shots} goals ({goals / shots:.1%})")


if __name__ == "__main__":
    main()
