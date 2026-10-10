def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}: {line!r}")
    city, temp, date = parts
    city = city.strip()
    temp = temp.strip()
    date = date.strip()
    if city == "" or date == "":
        raise ValueError(f"Пустое поле города или даты: {line!r}")
    temp = temp.replace(",", ".")
    try:
        temperature = float(temp)
    except ValueError:
        raise ValueError(f"Температура не число: {temp!r}")
    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if line.strip() == "":
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
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
    if not averages:
        return ""
    best = None
    for city in sorted(averages):
        if best is None or averages[city] > averages[best]:
            best = city
    return best