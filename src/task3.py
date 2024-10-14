def parse(raw: str) -> list[list[float]]:
    return [[float(f) for f in line.split()] for line in raw.split("|")]
