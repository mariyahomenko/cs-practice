import sys
from logstats import count_levels, top_errors, format_report


def main():
    path = sys.stdin.readline().strip()

    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)

    with open(path, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    total = sum(v for k, v in counts.items() if k != "BROKEN")
    errors_count = counts.get("ERROR", 0)
    broken = counts.get("BROKEN", 0)
    print(total)
    print(errors_count)
    print(broken)

    with open("report.txt", "w", encoding="utf-8") as out:
        out.write(format_report(counts, errors))


if __name__ == "__main__":
    main()
