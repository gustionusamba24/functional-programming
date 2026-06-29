def remove_invalid_lines(document: str) -> str:
    split_lines = document.split("\n")
    filtered_lines = filter(lambda line: not line.startswith("-"), split_lines)
    return "\n".join(filtered_lines)
