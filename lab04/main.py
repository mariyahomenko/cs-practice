import sys
from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)
    skipped = len(lines) - len(records)
    print(len(records))
    print(skipped)
    print(f"{average_by_city(records)[warmest_city(records)]:.1f}")


if __name__ == "__main__":
    main()