LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    parts = line.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError(f"Недостаточно полей: {line!r}")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"Незнакомый уровень: {level!r}")
    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if line.strip() == "":
            continue
        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            continue
        level = event["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n: int) -> list[list]:
    messages = {}
    for line in lines:
        if line.strip() == "":
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] != "ERROR":
            continue
        msg = event["message"]
        messages[msg] = messages.get(msg, 0) + 1
    pairs = [[msg, cnt] for msg, cnt in messages.items()]
    pairs.sort(key=lambda p: (-p[1], p[0]))
    return pairs[:n]
