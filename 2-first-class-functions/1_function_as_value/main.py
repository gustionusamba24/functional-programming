from collections.abc import Callable


def file_to_prompt(
    file: dict[str, str], to_string: Callable[[dict[str, str]], str]
) -> str:
    formatted_file = to_string(file)
    return f"```\n{formatted_file}\n```"
