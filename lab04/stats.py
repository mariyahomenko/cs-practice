def parse_record(line: str) -> dict:
    city, temp, date = line.split(";")
    return {"city": city, "temperature": float(temp), "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if line == "":
            continue
        records.append(parse_record(line))
    return records


def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for r in records:
        total[r["city"]] = total.get(r["city"], 0) + r["temperature"]
        count[r["city"]] = count.get(r["city"], 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    best = ""
    for city in averages:
        if best == "" or averages[city] > averages[best]:
            best = city
    return best