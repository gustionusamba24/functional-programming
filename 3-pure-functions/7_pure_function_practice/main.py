from collections.abc import Callable

default_commands: dict[str, Callable[..., object]] = {}
default_formats: list[str] = ["txt", "md", "html"]
saved_documents: dict[str, str] = {}

# Don't edit above this line


def add_custom_command(
    commands: dict[str, Callable[..., object]],
    new_command: str,
    function: Callable[..., object],
) -> dict[str, Callable[..., object]]:
    copied_commands = commands.copy()
    copied_commands[new_command] = function
    return copied_commands


def add_format(formats: list[str], format: str) -> list[str]:
    copied_formats = formats.copy()
    copied_formats.append(format)
    return copied_formats


def save_document(docs: dict[str, str], file_name: str, doc: str) -> dict[str, str]:
    copied_docs = docs.copy()
    copied_docs[file_name] = doc
    return copied_docs


def add_line_break(line: str) -> str:
    return line + "\n\n"
