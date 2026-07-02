from collections.abc import Callable


def word_count_aggregator() -> Callable[[str], int]:
    count = 0

    def inner_func(document: str) -> int:
        nonlocal count
        count += len(document.split())
        return count

    return inner_func