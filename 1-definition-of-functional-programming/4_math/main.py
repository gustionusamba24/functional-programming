def get_median_font_size(font_sizes: list[int]) -> int | None:
    if not font_sizes:
        return None

    return sorted(font_sizes)[(len(font_sizes) - 1) // 2]