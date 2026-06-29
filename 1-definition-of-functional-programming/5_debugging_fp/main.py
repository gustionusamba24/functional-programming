def format_line(line: str) -> str:
    # return f"{line.rstrip().capitalize().replace(',', '')}...."
    stripped_line = line.strip()
    capitalized_line = stripped_line.upper()
    formatted_line = capitalized_line.replace(".", "")
    return f"{formatted_line}..."