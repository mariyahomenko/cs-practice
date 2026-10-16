LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    parts = line.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError(f"Недостаточно полей: {line!r}")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"Незнакомый уровень: {level!r}")
    return {"time": time, "level": level, "message": message}
