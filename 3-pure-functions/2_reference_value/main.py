def add_format(default_formats: dict[str, bool], new_format: str) -> dict[str, bool]:
    copied_formats = default_formats.copy()
    copied_formats[new_format] = True
    return copied_formats


def remove_format(default_formats: dict[str, bool], old_format: str) -> dict[str, bool]:
    copied_formats = default_formats.copy()
    copied_formats[old_format] = False
    return copied_formats
