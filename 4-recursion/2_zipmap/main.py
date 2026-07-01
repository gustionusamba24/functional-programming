def zipmap(keys: list[str], values: list[float]) -> dict[str, float]:
    if len(keys) == 0 or len(values) == 0:
        return {}

    result: dict[str, float] = zipmap(keys[1:], values[1:])
    # keys = ['Rushmore', 'The Darjeeling Limited', 'The French Dispatch', 'The Wonderful Story of Henry Sugar and Three More']
    # values = [8.0, 7.2, 7.4, 7.3]
    result[keys[0]] = values[0]
    return result