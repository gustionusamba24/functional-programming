from collections.abc import Callable


def file_type_getter(
    file_extension_tuples: list[tuple[str, list[str]]],
) -> Callable[[str], str]:
    dict_file_types = {}
    for file_type, extensions in file_extension_tuples:
        for extension in extensions:
            dict_file_types[extension] = file_type

    return lambda ext: dict_file_types.get(ext, "Unknown")