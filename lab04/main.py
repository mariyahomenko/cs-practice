import sys
from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)
    skipped = len(lines) - len(records)
    print(len(records))
    print(skipped)
    if records:
        averages = average_by_city(records)
        print(f"{averages[warmest_city(records)]:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()